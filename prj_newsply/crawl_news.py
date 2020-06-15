import requests
import re
import datetime
import time
from bs4 import BeautifulSoup

from pymongo import MongoClient
# db = client.dbsparta

# selenium 동작
from selenium import webdriver
# driver = webdriver.Chrome('C:/Users/Go/Downloads/chromedriver')

client = MongoClient('localhost', 27017)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
lv1_data = requests.get(
    'https://news.daum.net/ranking/bestreply', headers=headers)

# soup = BeautifulSoup(lv1_data.text, 'html.parser')

# # 랭크 뉴스의 원문주소, 헤드라인 및 썸네일 주소 저장하기
# news_ranked = soup.select('div.rank_news > ul > li')

# for news in news_ranked:
#     # 헤드라인, 뉴스원문주소 및 뉴스ID 가져오기
#     a = news.select_one('div.cont_thumb > strong.tit_thumb > a')
#     if a is not None:
#         artUrl = a['href'] # article url
#         head = a.text # headline
#         news_id = re.findall("\d+", artUrl) # news ID
#         # news ID 에서 날짜 추출 및 datetime 으로 변환
#         year = int(news_id[0][:4]) # year indexing
#         month = int(news_id[0][4:6]) # month indexing
#         day = int(news_id[0][6:8]) # day indexing
#         myDay = datetime.date(year, month, day) 

#     # 썸네일 가져오기
#     i = news.select_one('a.link_thumb > img')
#     if i is not None:
#         thumb_url = i['src'] # thumbnail image
#         print(thumb_url)

#     # 덧글 가져오기

# driver.close()

# news_data 에서 가져온 top50 news 의 url 을 가지고, 해당 news 로 들어가서, 상위 3개의 덧글을 가져온다.
sel_url = 'https://news.v.daum.net/v/20200615050132469'
driver = webdriver.Chrome('C:/Users/Go/Downloads/chromedriver')

lv2_data = requests.get(sel_url, headers=headers)

#mArticle > div.foot_view > div.cmt_news.cmt_view
time.sleep(3)
soup2 = BeautifulSoup(lv2_data.text, 'html.parser')
time.sleep(3)
print(soup2)
# comments = soup2.select('ul.list_comment')
#comment538178455 > div > p
comments = soup2.select('#alex-area > div > div > div > div.cmt_box > ul.list_comment')
print(comments)
for comment in comments:
    a = comment.select_one('li > div.cmt_info > strong > p')
    if a is not None:
        print(a.text)
#comment537656461 > div > p
# for comment in comments :
#     print(comment.text)

#comment537422890 > div > p
#comment537422890 > div > p
driver.close()

