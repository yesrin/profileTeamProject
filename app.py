
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.y3rdt1e.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index2.html')

# 방명록저장
@app.route("/mars", methods=["POST"])
def mars_post():
    guest_receive = request.form['guest_give']
    doc={
        'guestcomment':guest_receive
    }
    db.guestbook.insert_one(doc)

    return jsonify({'msg':'방명록 등록완료!'})



# 맴버정보받아오기
@app.route("/member1", methods=["GET"])
def member1_get():
    users_data = list(db.member1.find({},{'_id':False}))
    return jsonify({'result':users_data})
@app.route("/member2", methods=["GET"])
def member2_get():
    users_data = list(db.member2.find({},{'_id':False}))
    return jsonify({'result':users_data})
@app.route("/member3", methods=["GET"])
def member3_get():
    users_data = list(db.member3.find({},{'_id':False}))
    return jsonify({'result':users_data})
@app.route("/member4", methods=["GET"])
def member4_get():
    users_data = list(db.member4.find({},{'_id':False}))
    return jsonify({'result':users_data})
#----------------------------------------------맴버정보 받아오기
# 방명록 받아오기
@app.route("/guest", methods=["GET"])
def guest_get():
    guest_data = list(db.guestbook.find({},{'_id':False}))
    return jsonify({'result':guest_data})
@app.route("/guest2", methods=["GET"])
def guest2_get():
    guest_data = list(db.guestbook.find({},{'_id':False}))
    return jsonify({'result':guest_data})
@app.route("/guest3", methods=["GET"])
def guest3_get():
    guest_data = list(db.guestbook.find({},{'_id':False}))
    return jsonify({'result':guest_data})
@app.route("/guest4", methods=["GET"])
def guest4_get():
    guest_data = list(db.guestbook.find({},{'_id':False}))
    return jsonify({'result':guest_data})

#------------------------------------------------
if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)


# from flask import Flask, render_template, request, jsonify
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route("/member1", methods=["POST"])
# def mars_post():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg':'POST 연결 완료!'})

# @app.route("/mars", methods=["GET"])
# def mars_get():
#     return jsonify({'msg':'GET 연결 완료!'})

# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)