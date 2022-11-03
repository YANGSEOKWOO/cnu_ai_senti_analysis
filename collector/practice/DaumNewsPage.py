import requests
from bs4 import BeautifulSoup
from collector.practice.CollectorService import get_daum_news

# 1페이지에서 15개의 뉴스(제목 ,본문) 수집 코드
# -> 1~끝페이지 돌면서 수집 수정!
# https://news.daum.net/breakingnews/?page=7
#-> 끝에 ? 뜨는거 / 쿼리스트링(QueryString) : url(주소) + data
# url ? data\
news_cnt = 0

for num in range(1,3):
    print(f'■■ {num}page ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    url = f'https://news.daum.net/breakingnews/?page={num}'  # 1page
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title_list = doc.select('ul.list_news2 a.link_txt')
    if title_list == 0:
        break
    for i, title in enumerate(title_list):
        print(f'인덱스:{i+1}, 제목: {title["href"]}')
        get_daum_news(title["href"])
        news_cnt += 1

print(f'총 {news_cnt}개의 뉴스를 수집하였습니다.')
