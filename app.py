from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(
    "mongodb+srv://sparta:test@cluster0.y3rdt1e.mongodb.net/?retryWrites=true&w=majority"
)
db = client.dbsparta

# 방명록 코멘트 등록

@app.route("/chat", methods=["POST"])
def chat_post():

    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    table_id_receive = request.form['table_id_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }

    db[table_id_receive].insert_one(doc)

    return jsonify({'msg':'작성 완료!'})

# 방명록 받아오기

@app.route("/chat", methods=["GET"])
def chat_get():
    table_id = request.args.get('table_id')
    chat_data = list(db[table_id].find({},{'_id':False}))
    return jsonify({'result':chat_data})

# 방명록 끝

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/team')
def start():
    return render_template('index2.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)