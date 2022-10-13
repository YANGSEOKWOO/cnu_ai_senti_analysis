# 주석!!!!!!!!!!!!!!!!!!!!!!!
# -> 개발자의 메모장, 파이썬이 주석은 실행 하지 않는다.
# 파이썬의 경로
# 1. 프로젝트(cnu.ai.senti.analysis-main)
#  └ 2.패키지(collector)
#   └ 3.Python file(test.py, DaumNewsOne.py)
# - python package : python file들을 모아두는 폴더
#                     폴더 아이콘안에 구멍 뚫려있음

# import와 Library(module)
# - Python 코드를 직접 작성해서 개발할수도 있지만
# - 다른 개발자가 이미 만들어 놓은 코드를 사용하면 편리함
# - 라이브러리(module) : 이미 개발되어있는 코드들의 묶음
#   1. built in library : Python 설치하면 자동으로 제공
#                           ex) math, sys, os 등
#   2. 외부 library : 우리가 직접 추가해서 사용!
#                   ex) requests, beautifulsoup4

# Library를 사용하기 위해서는 import 작업 진행
# -import는 도서관에서 필요한 책을 빌려오는 개념
import requests
# 책 전체를 빌려옴
from bs4 import BeautifulSoup
# bs4라는 책에서 BeautifulSoup 1개 파트만 빌려옴

# 목표 : Daum 뉴스 웹페이지 제목과 내용 데이터를 수집!
# 1) request로 해당 URL의 전체 소스코드를 가지고 온다.
# 2) Beautifulsoup에게 전체 소스코드 전달 -> doc
# 3) bs4가 전체소스코드에서 원하는 데이터만 select

# 1. url : https://v.daum.net/v/20221006080402550
url = 'https://v.daum.net/v/20221006080402550'
# 2. requests로 해당 url의 html 전체 코드를 수집!
# 2-1 client가 웹브라우저의 url을 다음뉴스 서버에 요청을 한다.(request)
# 2-2 Daumnews가 응답을 한다. (response), 성공했을경우 print하면 200이 뜬다.
result = requests.get(url)
# alt + shift 방향키 위로하면 옮길수 있다. (파이참가능)
# Response[200]이 뜬다면 성공했다는 의미, 저장을 하고 실행하기!, 인스타로 방탄게시물 좋아요 할 수 있도록도 가능

# 3.beautifulsoup를 통해서 '제목과 본문'만 추출
doc = BeautifulSoup(result.text, 'html.parser')
title = doc.select('h3.tit_view')[0].get_text()  # h3 태그 중에 이름이 tit_view를 갖는 select
# html -> tag + 선택자
# - tag : 기본적으로 정의 돼있음 (h3, p, div, span, ...)
contents = doc.select('section p')  # section 태그를 부모로 둔 모든 자식 p태그들 수집
# title, contents 에서 s의 차이 (단수와 복수의 차이)
# .get_text() text 값만 뽑아 준다.
# 자동완성 단축키 ctrl + space

print(f'뉴스제목: {title}')
# contents = [<p1>, <p2>, <p3>, <p4>, .....] : 복수의 본문 포함
# <p1> = <p> 블라블라블라 </p>

content = ''
for line in contents:
    content += line.get_text()
print(f'뉴스 본문: {content}')