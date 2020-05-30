# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/') # route : 방향을 정해준다는 의미
# def home():
#    return render_template('index.html')

# @app.route('/mypage')
# def mypage():  
#    return 'This is My Page!'

# @app.route('/index')
# def indexpage():  
#    return 'Index page'

# if __name__ == '__main__':  
#    app.run('0.0.0.0',port=5000,debug=True)

# static : 변화가 없는 파일들이란 의미에서 static 이란 이름을 사용
# templates 


# get 은 데이터를 "조회"할 때 사용
# 구글에서 인터스텔라를 조회한다. (HTML)
# 공공 데이터 오픈 API 에서 데이터를 가져온다 (JSON)
# 데이터를 URL 에 담아 보낸다
# www.google.com/?q="인터스텔라"

# post 는 데이터를 추가하고, 변경하고, 삭제하고
# 회원가입 -> 데이터를 추가함
# ID, PW 를 URL 에 포함시키면 안된다.
# 데이터를 body 안에 key:value 형태로 보낸다.
#  

# app.route('/index') 에서 안써주면 default 는 get method 이다.

# jsonify json 으로 데이터를 만들겠다는 의미

# reuest.args.get('ddd')  -> flask 에 정의된 명령
# args 란 곳에 get 에 의한 url 로부터의 요청값을 다 저장한다.

# 1. Ajax 로 get, post 요청 보내보기
# 2. "봄날은 간다" -> 다른 이름으로 바꿔서 테스트 해보기
# 3. title_give 변수를 다른 것으로 바꿔보기

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['message'] # post 요청은 form 으로 받고,
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('message') # get 요청은 args 로 받는다.
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

# 이러한 작업들은.... ajax 에서 어떤 변수를 보냈고, 서버에서 그것을 확인하는 작업을 하는 것

