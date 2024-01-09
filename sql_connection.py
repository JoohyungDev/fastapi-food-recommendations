from urllib.request import urlopen
from bs4 import BeautifulSoup

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='patrick7', 
                       db='foodDB', charset='utf8')

cur = conn.cursor()     # SQL문을 실행하거나 실행된 결과를 돌려받는 통로
# usertable 생성
# cur.execute("create table menutable (summer varchar(100),\
#             winter varchar(100), general varchar(100))")
# 데이터 입력(아직 임시 저장된 상태)
# cur.execute('insert into usertable values("hong","홍지윤",\
#             "hong@naver.com",1996)')

# 확실하게 저장(commit)
# conn.commit()

# 데이터 조회
sql = 'select summer from menutable'
cur.execute(sql)

# 데이터 여러줄 출력
for row in cur:
    print(row[0])

# 데이터 한줄 검색
# row = cur.fetchone()
# print(row[0], row[1], row[2], row[3])

# 데이터베이스를 모두 사용했다면?
# conn.close