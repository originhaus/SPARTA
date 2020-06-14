from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)

# uml diagram 을 찾아보기
# MarkDown 문법 알아보기 (readme.md 파일등이 github 에 있으니 참고)
# endpoint 를 기준으로 API table 을 작성한다.
# <button class="btn_g btn_recomm #like ?c_title=%EB%8C%93%EA%B8%80%EC%B0%AC%EC%84%B1" data-tiara-action-name="댓글_찬성" data-tiara-custom="alex.commentId=537629826" data-reactid=".0.0.0.3.2.$537629826.0.3.1.0"><span class="img_cmt ico_recomm bounce" data-reactid=".0.0.0.3.2.$537629826.0.3.1.0.0">댓글 찬성하기</span><span class="num_txt" data-reactid=".0.0.0.3.2.$537629826.0.3.1.0.1">15935</span></button>
