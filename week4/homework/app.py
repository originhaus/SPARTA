
# token 을 이용하여 로그인 기능 수행
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# request 는 데이터에 접근하기 위해서 임포트
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('/index_hw_4.html')  # render 란 index 를 그려준다는 의미

# API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def push_order():
    # 1. 클라이언트가 준 customer_name, order_number, delivery_address 가져오기.
    # customer name
    # print('complete')
    # customer_name = request.form['customer_name']
    name = request.form['customer_name']
    # order number
    delivery = request.form['order_delivery']
    # delivery address
    address = request.form['delivery_address']
    # phone number
    phone = request.form['phone_number']

    # 2. DB에 정보 삽입하기
    order = {
        'name': name,
        'delivery': delivery,
        'address': address,
        'phone': phone
    }
    db.orders.insert_one(order)

    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 작성되었습니다.'})

# API 역할을 하는 부분
@app.route('/order', methods=['GET'])
def pop_order():
    # 1. DB에서 리뷰 정보 모두 가져오기
    orders = list(db.orders.find({}, {'_id': 0}))
    # print('pop')
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'orders': orders}) # 오른쪽 orders 는 리스트 type

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# 이전 서버를 꺼야 새로운 프로젝트의 서버가 잘 동작될 수 있다.
# 폴더열기를 시도해보자


# 일반적으로 서버부터 만들고, 자바스크립트를 만든다
# 서버에서 정의한 규칙에 맞게 자바스크립트의 변수이름을 만든다
