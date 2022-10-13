import pprint

import requests

from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')  # result.text 파일을 html 형식의 파일로 바꾼다.print(doc)
# <a href="url"> : a 태그는 클릭했 을 때 해당 url 로 이동 한다.
# len(): list[]의 갯수를 알려 주는 함수
title_list = doc.select('ul.list_news2 a.link_txt')
# pprint.pprint(title_list)
# print(len(title_list))

# enumerate() : 반복 하면서 index 번호와 item 을 가져옴
# list[]의 index 는 0번부터 시작
# len(list) = 15, index = 0~14
for i, title in enumerate(title_list):
    print(f'인덱스:{i+1}, 제목: {title.get_text()}')
# href만 가져오고 싶다 -> title["href"]
# text만 가져오고 싶다 -> title.get_text()


