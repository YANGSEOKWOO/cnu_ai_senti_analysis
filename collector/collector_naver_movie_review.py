import requests
import re
import math
from bs4 import BeautifulSoup
from db.database import create_review


###################

# 1. 영화 제목 수집 #

###################

# movie_code : 네이버 영화 코드 (6자리 숫자)
# 제목 수집 / 네이버 에서 영화 리뷰창 가져온 다음에 code= 이후 부터 다 지움
#  - 1. 생성, 2. 호출
#  - 함수는 생성 하면 아무 동작 X
#  - 반드시 생성 후 호출을 통해서 사용!


def movie_title_crawler(movie_code):
    url = f'https://movie.naver.com/movie/bi/mi/basic.naver?code={movie_code}'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.h_movie > a')[0].get_text()
    return title


# 리뷰 수집 / 1. 평점 2. 내용 3. 작성자 4. 작성 일자 + 제목


def movie_review_crawler(movie_code):
    title = movie_title_crawler(movie_code)  # 제목 수집
    #  set {제목, 리뷰, 평점, 작성자, 작성 일자}
    # 리뷰를 수집 하는 코드 작성! (숙제!)
    print(f' >> Start collecting movies of {title}')

    url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after' \
          f'&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false' \
          f'&page=8 '
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    all_count = doc.select('strong.total > em')[0].get_text()  # 리뷰전체 수
    # 한 페이지 당 리뷰가 10개 !
    # ex) 문자열 로 되어 있다.
    # "2,480" -> 문자 포함 변환(X)

    # 1. 숫자만 추출 : 정규식
    numbers = re.sub(r'[^0-9]', '', all_count)
    pages = math.ceil(int(numbers) / 10)
    print(f'The total number of pages to collect is {pages}')

    # 해당 페이지 리뷰 수집
    count = 0  # 전체 리뷰 수를 count
    for page in range(1, pages + 1):
        url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after' \
              f'&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false' \
              f'&page={page}'
        result = requests.get(url)
        doc = BeautifulSoup(result.text, 'html.parser')
        review_list = doc.select('div.score_result > ul > li')  # 1page 리뷰 10건

        for i, one in enumerate(review_list):  # review 1건씩 수집
            # 리뷰, 평점, 작성자, 작성 일자 + 전처리
            review = one.select('div.score_reple > p > span')[-1].get_text().strip()
            score = one.select('div.star_score > em')[0].get_text()

            # 날짜 시간 -> 날짜만 추출
            # - 예 : 2022.10.19 15.28 -> 2022.10.19
            # - 날짜는 항상 16글자로 구성
            original_date = one.select('div.score_reple dt > em')[-1].get_text()
            date = original_date[:10]

            original_writer = one.select('div.score_reple dt > em')[0].get_text().strip()
            idx_end = original_writer.find('(')
            writer = original_writer[:idx_end]

            count += 1
            print(f"#########################################{count}번째 review"
                  f"###################################################")
            print(f'# Review: {review}')
            print(f'# Writer : {writer}')
            print(f'# Score : {score}')
            print(f'# Date : {date}')
            # Review 데이터 생성
            # -> 규격(포멧) -> JSON
            # JSON -> 데이터 주고받을 때 많이 사용하는 타입
            # MongoDB -> BSON(Binary JSON) = JSON
            # Python의 Dictionary = JSON
            #
            # ※ Python Dictionary = JSON = BSON
            # JSON 포멧
            # {key:value, Key:value, Key:value}

            # Dict type은 데이터 꺼낼 때 key값
            # List type은 데이터 꺼낼 때 index값
            data = {
                'title': title,
                'score': score,
                'review': review,
                'writer': writer,
                'date': date
            }
            create_review(data)
