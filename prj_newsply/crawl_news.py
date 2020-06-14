import requests
import re
from bs4 import BeautifulSoup

from pymongo import MongoClient
# db = client.dbsparta

from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Go/Downloads/chromedriver')



client = MongoClient('localhost', 27017)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
lv1_data = requests.get(
    'https://news.daum.net/ranking/bestreply', headers=headers)

soup = BeautifulSoup(lv1_data.text, 'html.parser')

# 랭크 뉴스의 원문주소와 헤드라인 저장하기
# news_ranked = soup.select('div.rank_news > div.cont_thumb > strong')
# print(news_ranked)
# news_ranked = soup.select('div.rank_news')
# news_ranked = soup.select('#mArticle > div.rank_news > div.cont_thumb')
# news_ranked = soup.select('.news_list > div.cont_thumb > strong')
# news_ranked = soup.select('.cont_thumb > strong')
news_ranked = soup.select('div.rank_news > ul > li > div.cont_thumb > strong')
# print(news_ranked)
#mArticle > div.rank_news
urls = []
# 헤드라인 뉴스의 주소를 가져오기
for news_data in news_ranked:
    a = news_data.select_one('.tit_thumb > a')
    if a is not None:
        url = a['href'] # 헤드라인 주소와,
        head = a.text # 헤드라인 제목을 불러와서,
        news_id = re.findall("\d+", url)
        # base_url = url - news_id
        # print(news_data)
#        print(head)
        # print(url)
#        print(news_id)
        # print(base_url)
        # base url 과 news 번호를 분리하는 코드 작성하기
        # 오늘날짜는 news 번호의 앞 8자리 숫자이므로, 별도 날짜 생성하여 저장할 필요 없음
        # top news 50 은 특정 시간 (?) 단위로 업데이트 된다.

# print(url)
# news_data 에서 가져온 top50 news 의 url 을 가지고, 해당 news 로 들어가서, 상위 3개의 덧글을 가져온다.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# base_data = requests.get(
#     'http://v.media.daum.net/v/20200613142311949', headers=headers)

sel_url = 'http://v.media.daum.net/v/20200613142311949'
driver.get(sel_url)

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

comments = soup.select('p.desc_txt')

# for comment in comments:
#     a = comment.select_one('p.desc_txt')
#     if a is not None:
#         print(a.text)
#comment537656461 > div > p
# for comment in comments :
#     print(comment.text)

#comment537422890 > div > p
#comment537422890 > div > p

# for news_data in lv2_data:
#     #comment537629826 > div > p
#     #comment537630017 > div > p
#     #a = news_data.select_one('div.cmt_info > strong.tick_nick > p')
#     p = news_data.select_one('p.desc_txt font_size')
#     if p is not None:
#         head = a.text # 헤드라인 제목을 불러와서,
#         print(head)
#         # print(url)
#         # base url 과 news 번호를 분리하는 코드 작성하기
#         # 오늘날짜는 news 번호의 앞 8자리 숫자이므로, 별도 날짜 생성하여 저장할 필요 없음
#         # top news 50 은 특정 시간 (?) 단위로 업데이트 된다.
driver.close()

