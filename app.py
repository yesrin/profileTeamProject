from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(
    "mongodb+srv://sparta:test@cluster0.y3rdt1e.mongodb.net/?retryWrites=true&w=majority"
)
db = client.dbsparta
#팀원정보 받아오기
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

#팀원 사진 받아오기
@app.route("/image1", methods=["GET"])
def image_get1():
    image_data = list(db.image.find({},{'_id':False}))
    return jsonify({'result':image_data})
@app.route("/image2", methods=["GET"])
def image_get2():
    image_data = list(db.image.find({},{'_id':False}))
    return jsonify({'result':image_data})
@app.route("/image3", methods=["GET"])
def image_get3():
    image_data = list(db.image.find({},{'_id':False}))
    return jsonify({'result':image_data})
@app.route("/image4", methods=["GET"])
def image_get4():
    image_data = list(db.image.find({},{'_id':False}))
    return jsonify({'result':image_data})



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

# @app.route("/mars", methods=["POST"])
# def mars_post():
#     name_receive = request.form['name_give']
#     address_receive = request.form['address_give']
#     size_receive = request.form['size_give']

#     doc = {
#         'name': name_receive,
#         'address': address_receive,
#         'size': size_receive
#     }

#     db.mars.insert_one(doc)

#     return jsonify({'msg': '주문 완료!'})

# @app.route("/mars", methods=["GET"])
# def mars_get():
#     mars_data = list(db.mars.find({},{'_id':False}))
#     return jsonify({'result':mars_data})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)