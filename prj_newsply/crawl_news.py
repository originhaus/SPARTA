import requests
import re
import datetime
import time
from bs4 import BeautifulSoup

from pymongo import MongoClient
# db = client.dbsparta

# selenium 동작
from selenium import webdriver
# driver = webdriver.Chrome('C:/Users/Go/Downloads/chromedriver.exe')

client = MongoClient('localhost', 27017)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
lv1_data = requests.get(
    'https://news.daum.net/ranking/bestreply', headers=headers)

soup = BeautifulSoup(lv1_data.text, 'html.parser')

# 랭크 뉴스의 원문주소, 헤드라인 및 썸네일 주소 저장하기
news_ranked = soup.select('div.rank_news > ul > li')

for news in news_ranked:
    # 헤드라인, 뉴스원문주소 및 뉴스ID 가져오기
    a = news.select_one('div.cont_thumb > strong.tit_thumb > a')
    if a is not None:
        artUrl = a['href'] # article url
        head = a.text # headline
        news_id = re.findall("\d+", artUrl) # news ID
        # news ID 에서 날짜 추출 및 datetime 으로 변환
        year = int(news_id[0][:4]) # year indexing
        month = int(news_id[0][4:6]) # month indexing
        day = int(news_id[0][6:8]) # day indexing
        myDay = datetime.date(year, month, day) 

    # 썸네일 가져오기
    i = news.select_one('a.link_thumb > img')
    if i is not None:
        thumb_url = i['src'] # thumbnail image
        print(thumb_url)

# news_data 에서 가져온 top50 news 의 url 을 가지고, 해당 news 로 들어가서, 상위 3개의 덧글을 가져온다.
sel_url = 'https://news.v.daum.net/v/20200615050132469'
# selenium 동작
driver = webdriver.Chrome('C:/Users/Go/Downloads/chromedriver.exe')
driver.get(sel_url) # chrome 에 url 을 넣고

time.sleep(3) # 3초간 프로세스를 일시정지하고,

req = driver.page_source # 페이지의 소스코드를 저장한 후,

time.sleep(3) # 3초간 프로세스를 일시정지하고,

soup2 = BeautifulSoup(req, 'html.parser') # lv2_data 의 text 를 html parsing 후, soup2 라 한다.
time.sleep(3) # 3초간 프로세스를 일시정지하고,
comments = soup2.select('#alex-area > div > div > div > div.cmt_box > ul.list_comment > li') # ul.list_comment 아래단계의 li 가 담긴 구문을 모두 선택한다
for comment in comments:
    a = comment.select_one('p.desc_txt') # 선택된 li 구문 중에 p.desc_txt 를 찾는 것을 반복한다.
    if a is not None:
        comment = a.text.replace("\n", " ") # 줄바꿈 기호를 공백으로 바꾸고,
        # 코멘트의 스크래핑 날짜 기준 추천순위를 나열한다. dictionary 로 ? 
        # [{뉴스키 : 뉴스키값}, 
        #  {날짜 : 날짜값}, 
        #  {헤드라인 : 헤드라인값}
        #  {조회수 : 조회수값, 코멘트 : 코멘트 내용},
        #  {조회수 : 조회수값, 코멘트 : 코멘트 내용},
        #  {조회수 : 조회수값, 코멘트 : 코멘트 내용}]
        print(comment)

driver.close()

