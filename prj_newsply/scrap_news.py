import requests
import re
import datetime
import time
import codecs
import pandas as pd
from pymongo import MongoClient
from bs4 import BeautifulSoup
from IPython.display import display

# # data frame 예제 출력
# my_dict = {"a": ['1', '3'], "b": ['1', '2'], "c": ['2', '4']}
# display(pd.DataFrame(my_dict))


# mongo db 연결
# db = client.dbsparta
# client = MongoClient('localhost', 27017)

positive = []
negative = []
posneg = []
pos = codecs.open("./positive.txt", 'rb', encoding='UTF-8')
while True : 
    line = pos.readline()
    line = line.replace('\n', '')
    positive.append(line)
    posneg.append(line)

    if not line : break
pos.close()

neg = codecs.open("./negative.txt", 'rb', encoding='UTF-8')
while True : 
    line = neg.readline()
    line = line.replace('\n', '')
    negative.append(line)
    posneg.append(line)

    if not line : break
neg.close()



# j = 0

# selenium 동작
from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
lv1_data = requests.get(
    'https://news.daum.net/ranking/bestreply', headers=headers)
soup = BeautifulSoup(lv1_data.text, 'html.parser')
# 랭크 뉴스의 원문주소, 헤드라인 및 썸네일 주소 저장하기
news_ranked = soup.select('div.rank_news > ul > li')
driver = webdriver.Chrome('C:/Users/Go/Downloads/chromedriver.exe')


# label = [0] * 40
# comment_dic = {'title':[], 'label':label}
comment_dic = {'title':[]}
j = 0
def get_comments(sel_url):
    driver.get(sel_url) # chrome 에 url 을 넣고

    time.sleep(3) # 3초간 프로세스를 일시정지하고,

    req = driver.page_source # 페이지의 소스코드를 저장한 후,

    # time.sleep(3) # 3초간 프로세스를 일시정지하고,

    soup2 = BeautifulSoup(req, 'html.parser') # lv2_data 의 text 를 html parsing 후, soup2 라 한다.

    # time.sleep(3) # 3초간 프로세스를 일시정지하고,
    comment_list = []
    comments = soup2.select('#alex-area > div > div > div > div.cmt_box > ul.list_comment > li') # ul.list_comment 아래단계의 li 가 담긴 구문을 모두 선택한다

    for comment in comments:
        a = comment.select_one('p.desc_txt') # 선택된 li 구문 중에 p.desc_txt 를 찾는 것을 반복한다.
        if a is not None:
            comment_num = 0
            comment = a.text.replace("\n", " ") # 줄바꿈 기호를 공백으로 바꾸고,
            comment = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》]', '', comment) # 정규식으로 문자외의 것들을 제거하고,
            comment_list.append(comment)
            # comment_list += comment
            # print(len(comment_list)) # 이렇게 하면 3개의 덧글이 출력되는데, 왜 return 하면 덧글 3개가 출력되지 않는 것일까
            # 3개의 comment 를 읽어들이므로, 3번 출력될 수 있도록 한다.            
            # print(comment_list) # 이렇게 하면 3개의 덧글이 출력되는데, 왜 return 하면 덧글 3개가 출력되지 않는 것일까
            # print(len(comment))
            # print(len(comment_list)) # 이렇게 하면 3개의 덧글이 출력되는데, 왜 return 하면 덧글 3개가 출력되지 않는 것일까
            # 3개 덧글을 한개의 리스트에 저장후 리스트를 반환하자.
            # print(len(comment_list))
            # for i in range(len(posneg)):
            #     posflag = False
            #     negflag = False
            #     if i < (len(positive)-1):
            #         print(comment.find(posneg[i]))
            #         if comment.find(posneg[i]) != -1 :
            #             posflag = True
            #             print(i, "positive?", "테스트 : ", comment.find(posneg[i]), "비교단어 : ", posneg[i], "인덱스 : ", i, comment)
            #             break
            #     if i > (len(negative)-2):
            #         if comment.find(posneg[i]) != -1:
            #             negflag = True 
            #             print(i, "negative?","테스트 : ",comment.find(posneg[i]),"비교단어 : ", posneg[i], "인덱스 : ", i, comment) 
            #             break
            # if posflag == True:
            #     label[j] = 1
            # elif negflag == True:
            #     label[j] = -1
            # elif negflag == False and posflag == False:
            #     label[j] = 0
            # j = j + 1

            comment_dic['title'].append(comment)
            print(comment_dic)
    # comment_df = pd.DataFame(comment_dic)
    # display(comment_df)
    return comment_list[0], comment_list[1], comment_list[2] 


# def df2csv(title_df, num):
#     title_df.to_csv(('./comment'+str(num)+'.csv'), sep=',', na_rep='NaN', encoding='UTF-8')

def get_metas(artUrl):
    # meta 스크래핑
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # print(artUrl)
    lv2_data = requests.get(artUrl, headers=headers)
    meta_soup = BeautifulSoup(lv2_data.text, 'html.parser') # lv2_data 의 text 를 html parsing 후, meta_soup 라 한다.
    og_image = meta_soup.select_one('meta[property="og:image"]') # og_image : property 의 og:image 에 해당하는 text 가져오기
    og_title = meta_soup.select_one('meta[property="og:title"]') # og_title : property 의 og:title 에 해당하는 text 가져오기
    og_description = meta_soup.select_one('meta[property="og:description"]') # og_description : property 의 og:description 에 해당하는 text 가져오기
    # print(og_image['content'])
    # print(og_title['content'])
    # print(og_description['content'])
    return og_image['content'], og_title['content'], og_description['content']


# # meta scraping test
# meta_info = 'http://v.media.daum.net/v/20200619174103728'
# lv3_data = requests.get(meta_info, headers=headers)
# meta_soup = BeautifulSoup(lv3_data.text, 'html.parser') # lv2_data 의 text 를 html parsing 후, soup2 라 한다.

# 새로운 덧글 및 뉴스는 중복을 피하기 위해, 기존 newsply db 에 중복 여부를 조회 후 저장한다.
head = ''
news_id = 0
myDay = datetime
for news in news_ranked:
    # 썸네일 가져오기
    i = news.select_one('a.link_thumb > img')
    if i is not None:
        thumb_url = i['src'] # thumbnail image
        print(thumb_url)

    # 헤드라인, 뉴스ID 가져오기
    a = news.select_one('div.cont_thumb > strong.tit_thumb > a')
    if a is not None:
        artUrl = a['href'] # article url
        head = a.text # headline
        news_id = re.findall("\d+", artUrl) # news ID
        # news ID 에서 날짜 추출 및 datetime 으로 변환
        year = int(news_id[0][:4]) # year indexing
        month = int(news_id[0][4:6]) # month indexing
        day = int(news_id[0][6:8]) # day indexing
        myDay = datetime.date(year, month, day) # 기사작성일자를 datatime 형태로 변환
        metas = get_metas(artUrl) # 메타스크래핑
        print(metas)
        comments = get_comments(artUrl) # 덧글 스크래핑 함수 호출
        # print(comments)

# 워드클라우드 만들기
# 시간 남을 때 하자.... ㅠ
# 형태소를 나눈 후, 명사 및 동사만을 가지고 클라우드를 만든다
# 덧글로 클라우드를 만들기보단, meta 제목 또는 설명을 가지고 만드는 것을 고려한다.


# # news_data 에서 가져온 top50 news 의 url 을 가지고, 해당 news 로 들어가서, 상위 3개의 덧글을 가져온다.
# sel_url = 'https://news.v.daum.net/v/20200615050132469'
# # selenium 동작
# driver = webdriver.Chrome('C:/Users/Go/Downloads/chromedriver.exe')
# driver.get(sel_url) # chrome 에 url 을 넣고

# time.sleep(3) # 3초간 프로세스를 일시정지하고,

# req = driver.page_source # 페이지의 소스코드를 저장한 후,

# time.sleep(3) # 3초간 프로세스를 일시정지하고,

# soup2 = BeautifulSoup(req, 'html.parser') # lv2_data 의 text 를 html parsing 후, soup2 라 한다.
# time.sleep(3) # 3초간 프로세스를 일시정지하고,
# comments = soup2.select('#alex-area > div > div > div > div.cmt_box > ul.list_comment > li') # ul.list_comment 아래단계의 li 가 담긴 구문을 모두 선택한다
# for comment in comments:
#     a = comment.select_one('p.desc_txt') # 선택된 li 구문 중에 p.desc_txt 를 찾는 것을 반복한다.
#     if a is not None:
#         comment = a.text.replace("\n", " ") # 줄바꿈 기호를 공백으로 바꾸고,
#         # 코멘트의 스크래핑 날짜 기준 추천순위를 나열한다. dictionary 로 ? 
#         # [{뉴스키 : 뉴스키값}, 
#         #  {날짜 : 날짜값}, 
#         #  {헤드라인 : 헤드라인값}
#         #  {조회수 : 조회수값, 코멘트 : 코멘트 내용},
#         #  {조회수 : 조회수값, 코멘트 : 코멘트 내용},
#         #  {조회수 : 조회수값, 코멘트 : 코멘트 내용}]

#         print(comment)

# 키, 작성일자, 헤드라인, 
# 덧글의 공감수(추천수)는 실시간으로 변하기 때문에, 저장하는게 무슨 의미가 있을까? 궁금할 경우, 원문보기로 해당 뉴스를 직접 보면 된다.
# 덧글 많은 뉴스에 랭크될 만큼 충분히 추천을 받았기 때문에, 그것을 세는 것은 큰 의미가 없을 것 같다.
# 3개의 덧글을 모두 긍정/부정 분석하기 보다는 최고 추천수의 덧글 하나의 형태소를 분석하고, 그것이 긍정의 덧글일 경우, 
# 디스플레이하고 그렇지 않을 경우 디스플레이 하지 않는 방법은 어떠한가.
# 또는 3개의 덧글을 모두 긍정/부정 분석한 후 상대적으로 긍정의 덧글이라고 판단될 경우, 해당 뉴스를 디스플레이하고, 그렇지 않을 경우, 
# 해당 뉴스 자체를 디스플레이 하지 않는 것은 어떠한가.


driver.close()


# 정보 공유 웹사이트
# 생활코딩, 페이스북, React Korea, 모각코, 원티드
# 링크드인, 블라인드, 패스트캠퍼스, 

# news 를 쇼핑하는 것과 같이, 마치 장바구니가 있는 것처럼 보이는 페이지 뷰
