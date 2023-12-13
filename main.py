from flask import Flask,render_template,request,url_for
import pickle
anime_sort_rating=pickle.load(open('sort_rating.pkl','rb'))
anime_sort_watching=pickle.load(open('sort_watching.pkl','rb'))
anime=pickle.load(open('ani.pkl','rb'))
indices=pickle.load(open('indicies.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/index2')
def index2():
    with open('sort_rating.pkl', 'rb') as f:
        data = pickle.load(f)
    return render_template('index2.html', data=data)
@app.route('/index1')
def index1():
    with open('sort_watching.pkl', 'rb') as f:
        data1 = pickle.load(f)
    return render_template('index1.html', data=data1)
@app.route('/recommended')
def recommended_ui():
    return render_template('recommended.html')
@app.route('/recommend_anime',methods=['post'])

def print_similar_animes():
    user_input = request.form.get('user_input')
    l = []
    item = []
    print("hi")
    found_id = anime[anime["name"]==user_input].index.tolist()[0]
    for id in indices[found_id][1:]:
        l.append(anime.iloc[id]["name"])
        l.append(anime.iloc[id]["rating"])
    for i in range(0, len(l), 2):
        item.append([l[i], l[i + 1] if i + 1 < len(l) else None])
    print(item)
    return render_template('recommended.html',data=item)
if __name__=='__main__':
    app.run(debug=True)
