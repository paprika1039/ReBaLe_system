from flask import Flask, render_template, request, session
from flask_session import Session
import program.hoge as hoge
# import program.make_sent_find_pkg as make_sentence
import program.word2vec_pkg as word2vec
import program.create_neo4j_remake as neo4j
from gensim import models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

w2v_model = models.KeyedVectors.load_word2vec_format('/Users/eguchibun/flask/pythonProject/program/jawiki.txt', binary=False)

@app.route('/')
def helo():
    return "hello world"

@app.route('/home', methods=["GET", "POST"])
def home():
    if(request.method == 'POST'):# リクエストがPOSTの場合
        username = request.form['username']
        session['username'] = username
        return render_template('home1.html')# challengeをhome.htmlに送る
    return render_template('signup.html')

# @app.route('/home', methods=['POST'])
# def login():
#     username = request.form['username']
#     # ユーザー名をセッションに保存
#     session['username'] = username
#     return 'Logged in successfully'

@app.route("/home1", methods=["GET", "POST"])
def home1():
    username = session.get("username")
    if (username): render_template("signup.html")
    button_text = "送信"
    if (request.method == 'POST'):  # リクエストがPOSTの場合
        button_text = "読み込み中です"
        challenge = request.form.get('challenge')  # challenge(社会課題)を取得
        # ユーザー名をセッションに保存
        session['username'] = username
        goodbye = hoge.goodbye()
        keyword = word2vec.auto_word2vec(challenge, w2v_model)
        neo4j.create_tree(keyword, username, challenge)
        # sentence = make_sentence.make_sentence_find(challenge)
        return render_template('result.html', challenge=challenge, goodbye=goodbye, keyword=keyword,
                               username=username)  # challengeをhome.htmlに送る
    return render_template("home1.html")

@app.route('/result')
def profile():
    # セッションからユーザー名を取得
    username = session.get('username')
    # return f'Username: {username}'
    return render_template(username=username)

if __name__ == '__main__':
    app.run(debug=True)

