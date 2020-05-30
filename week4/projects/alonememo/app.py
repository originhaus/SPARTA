from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    meta_datas = list(db.meta_datas.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'meta_datas': meta_datas})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
	# 1. 클라이언트로부터 데이터를 받기
    url_recive = request.form['url']
    comment_recive = request.form['comment']
    print(url_recive)
    print(comment_recive)
	# 2. meta tag를 스크래핑하기
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_recive,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    og_title = soup.select_one('meta[property="og:title"]')
    og_image = soup.select_one('meta[property="og:image"]')
    og_description = soup.select_one('meta[property="og:description"]')
    print(og_title['content'])
    print(og_image['content']) # beautiful soup 에서 og_image['content'] 이런식으로 쓰라고 하기에 이렇게 사용한다.
    print(og_description['content'])
	# 3. mongoDB에 데이터 넣기
    meta_data = {
        'url': url_recive,
        'comment': comment_recive,
        'title': og_title['content'], 
        'image': og_image['content'], 
        'desc' : og_description['content']
        }
    # meta_datas 에 review 저장하기
    db.meta_datas.insert_one(meta_data)
    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

# tailwindcss, tachyons 등의 템플릿도 있다.