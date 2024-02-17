# FastAPI를 활용한 음식 추천 서비스
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/-NvLj4?referralCode=CRJ8FE)

## 1. 개발 환경
- Python 3
- FastAPI
- Mysql

## 2. 설계
- 네이버에서 서울의 날씨와 온도를 가져옵니다.
- 현재 날씨, 온도, 계절에 따라 음식을 추천해줍니다.
- 비 / 눈 / 맑음 / 아침 / 점심 / 저녁 / 기타로 분류됩니다.

## 3. 사용법
- `pip install -r requirements.txt` : pip를 사용하여 설정된 환경을 설치합니다. 
- `uvicorn main:app --reload` : 로컬환경에서 해당 명령어를 사용하여 실행 가능합니다.
- `http://localhost:8000/recommend` : 로컬환경에서 해당 URL을 사용하여 접속 가능합니다.
