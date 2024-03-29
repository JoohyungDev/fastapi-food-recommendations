import random
import pymysql
from fastapi import FastAPI
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = FastAPI()

# 데이터베이스 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='비공개', 
                       db='foodDB', charset='utf8')
# SQL문을 실행하거나 실행된 결과를 돌려받는 통로
curs = conn.cursor()

@app.get("/recommend")

def recommend_food():
    current_hour = datetime.now().hour
    current_month = datetime.now().month

    # 네이버에서 서울의 날씨와 온도 정보를 가져오는 함수
    def get_weather_and_temp():
        url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hBftLdp0J14ssEH3W3VssssstxV-258497"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        temperature = soup.find(class_='temperature_text') 
        weather = soup.find(class_='weather before_slash')
        return weather.text, temperature.text

    # 현재 날씨, 온도, 계절에 따른 음식 추천을 반환하는 함수
    def recommend_by_weather_and_season(weather, temperature, month):
        if '비' in weather or '눈' in weather or month in [12, 1, 2]:  # 비나 눈이 오거나 겨울인 경우
            curs.execute("SELECT winter FROM menutable ORDER BY RAND() LIMIT 1;")
            menu = curs.fetchone()[0]
        elif '맑음' in weather and int(temperature.replace('℃', '')) > 25 and month in [6, 7, 8]:  # 맑고 25도 이상이며 여름인 경우
            curs.execute("SELECT summer FROM menutable ORDER BY RAND() LIMIT 1;")
            menu = curs.fetchone()[0]
        else:  # 그 외의 경우
            curs.execute("SELECT general FROM menutable ORDER BY RAND() LIMIT 1;")
            menu = curs.fetchone()[0]
        return menu

    weather, temperature = get_weather_and_temp()

    if 6 <= current_hour < 11:  # 아침
        menu = recommend_by_weather_and_season(weather, temperature, current_month)
        return {"recommendation": f"아침 메뉴: {menu}"}
    elif 11 <= current_hour < 15:  # 점심
        menu = recommend_by_weather_and_season(weather, temperature, current_month)
        return {"recommendation": f"점심 메뉴: {menu}"}
    elif 17 <= current_hour < 21:  # 저녁
        menu = recommend_by_weather_and_season(weather, temperature, current_month)
        return {"recommendation": f"저녁 메뉴: {menu}"}
    else:  # 그 외의 시간
        menu = recommend_by_weather_and_season(weather, temperature, current_month)
        return {"recommendation": f"메뉴: {menu}"}


# 라이브러리 설치
# pip install fastapi
# pip install uvicorn
    
# uvicorn main:app --reload 터미널에 입력 후 하단 주소 방문
# http://localhost:8000/recommend
