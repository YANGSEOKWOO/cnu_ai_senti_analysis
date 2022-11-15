from pymongo import MongoClient


# 회원
# - 회원가입(Create)
# - 회원수정(Update)
# - 회원삭제(Delete)
# - 회원목록(Select)

# 상품
# - 상품등록(Create)
# - 상품목록(Select)
# - 상품수정(Update)
# - 상품삭제(Delete)

# 게시판
# - 게시글등록(Create)
# - 게시글목록(Update)
# - 게시글수정(Delete)
# - 게시글삭제(Select)

# -> CRUD 작업    DA0(Data Access Object) 만듬
# 게시글 -> BoardA0.py
# 회원 -> MemberDA0.py


# 진짜 코드!

# 1. Connection 작업(공통:Common)
def db_conn():
    client = MongoClient('127.0.0.1', 27017)  # MongoDB 찾아감
    db = client['movie']                      # Database 선택
    collection = db.get_collection('review')  # Collection 선택
    return collection


# 2. Review 저장(Create)
def create_review(data):
    collection = db_conn()  # MongoDB Connection
    collection.insert_one(data)                 # 1건의 데이터를 저장!


# 3. Review 조회(Read)
def read_review():
    pass
