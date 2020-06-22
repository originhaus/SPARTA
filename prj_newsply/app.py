from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def comments_list():
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 오늘날짜를 기준으로, 추천수가 많은 덧글순으로 쿼리하는 것을 확인하기
    # 날짜정보를 받아서, db 조회에 사용
    search_date = request.args.get('date_give') # 날짜정보 받아오기
    newsplies = list(db.newsply.find({'date':search_date},{'display':'On'}, {'_id': False}).sort('posneg', -1)) # 긍정이 많은 덧글 순으로 불러오는 쿼리 필요
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 comments 목록을 클라이언트에 전달합니다.
    # news id 를 db로부터 가져오면 원문주소를 만들어주기 필요
    return jsonify({
        'result': 'success',
        'msg': 'comments_list 연결되었습니다!',
        'newsplies': newsplies
    })

@app.route('/api/list', methods=['POST'])
def comments_unlist():
    # 1. Display off 시킬 newsply 의 id 를 받기
    key = request.form('id_give') # Display off 시킬 newsply id 받기
    db.newsply.update_one({'key':key},{'$set':{'display':'off'}}) # 
    today = request.form('today_give')
    # 2. 오늘날짜를 기준으로, 긍정 덧글이 많은 덧글순으로 쿼리하는 것을 확인하기
    # 오늘날짜는 html 의 javascript 에서 news_id 를 쪼개어 받기
    # db 에 날짜를 string 변수를 만들어 으로 입력한 후 조회할 것
    # 날짜정보를 받아서, db 조회에 사용
    # display off 될 newsply 를 제외하고, 받아오기
    search_date = request.form('date_give') # 날짜정보 받아오기
    newsply = list(db.newsply.find({'date':search_date}, {'display':'On'}, {'_id': False}).sort('posneg', -1))
    # 2. 성공하면 success 메시지와 함께 comments 목록을 클라이언트에 전달합니다.
    # news id 를 db로부터 가져오면 원문주소를 만들어주기 필요
    return jsonify({
        'result': 'success',
        'msg': 'comments_unlist 연결되었습니다!',
        'newsply': newsply
    })

@app.route('/api/unroll', methods=['POST'])
def meta_news():
    # 기사 원문을 스크래핑하여 보여준다. db 에 저장할 필요 없음.
    # 받아온 기사의 key(id) 를 가지고 스크래핑.
    # 한번 스크래핑했으면 다시 클릭해도 스크래핑하지 않도록 flag 를 띄운다.
    # 1. news 의 id 를 받는다.
    key = request.form['id_give']
    # 2. news id 로 스크래핑 함수를 불러온다.
    meta_data = metaScrap() # 스크래핑 함수는 3가지의 meta data 를 반환해야 한다.

    # 3. meta_data 를 반환하기 위한 조작

    # 4. 스크래핑 결과를 되돌려준다.
    return jsonify({
        'result': 'success',
        'msg': 'meta_news 연결되었습니다'
        'meta_data' : meta_data
    })

# POST 요청은 리소스를 조작할 때, 리소스를 새로 만들 때(리소스의 변경) 사용
# db 의 내용이 변경 <- 리소스의 변경이 일어났다.

@app.route('/api/scrap_view', methods=['GET'])
def scrap_view():
    return jsonify({
        'result': 'success',
        'msg': 'scrap_view 연결되었습니다!'
    })


@app.route('/api/scrap', methods=['POST'])
def scraping():
    # 1. 클라이언트가 전달한 id_give를 id_receive 변수에 넣습니다.
    key = request.form['id_give']
    scrap_status = request.form['scrap_give'] # scrap_status 에는 scrap 설정/해제의 정보가 담김.

    if scrap_status is True:
        db.newsply.update_one({'key':key},{'$set':{'scrap':True}}) # 
    else:
        db.newsply.update_one({'key':key},{'$set':{'scrap':False}}) # 
    # 참고: '$set' 활용하기!
    return jsonify({
        'result': 'success',
        'msg': 'scraping 연결되었습니다!'
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
