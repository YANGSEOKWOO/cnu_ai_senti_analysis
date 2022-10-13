import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/article/658/0000022075?cds=news_media_pc&type=editn'
# ↓↓↓↓↓ 기계가 아니라 인간이라고 눈속임 하는 것 ↓↓↓↓↓↓
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, liek Gecko) Chrome/92.0.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')
# [0] 대괄호 제거
# .get_text() tag 제거하고 text만 추출
title = doc.select('h2.media_end_head_headline')[0].get_text()
content = doc.select('div#dic_area')[0].get_text().strip()
# strip() 앞뒤 공백 제거
print(f'본문:{title}')  # fstring
print('내용: {}'.format(content))  # format