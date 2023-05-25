# 오월엔 데브콘 in DAEJEON

* 장소 : 모두의 연구소 대전캠퍼스
* 일시 : 2023년 05월 27일 (토), 오후 01:00 - 오후 05:00
* 주관 : [K-DEVCON](https://festa.io/hosts/1880)
* 행사 페이지 : https://festa.io/events/3467

## 장고 채널스와 함께 Chat GPT 영어 상황극 채팅 서비스 만들기

* 발표자 : 이진석 - me@pyhub.kr

### 구동할려면?

1. [OpenAI API Keys](https://platform.openai.com/account/api-keys) 페이지에서 API KEY를 발급받습니다.
2. manage.py가 있는 경로에 `.env` 파일을 생성하고, 아래와 같이 내용을 구성합니다. `OPENAI_API_KEY` 항목에 발급받은 키를 지정해주세요.

```
# 개발 목적의 OPEN API 키를 지정합니다.
OPENAI_API_KEY=sk-*************************************VnU

# 장고 디폴트 안내 메세지를 한국어로 설정합니다.
LANGUAGE_CODE=ko-kr
```

3. 가상환경 생성/활성화 후에, 라이브러리 설치

```
python -m pip install -r requirements.txt
```

4. superuser 계정을 생성합니다.

```
python manage.py createsuperuser
```

5. 장고 개발서버를 구동합니다. 디폴트로 8000포트로 구동됩니다.

```
python manage.py runserver
```

6. 브라우저로 http://localhost:8000/ 주소로 접속합니다.

## About

* 이진석 <me@pyhub.kr>
* [페이스북 파이썬 사랑방 with Django/React 그룹](https://www.facebook.com/groups/askdjango)
* [인프런 프로필](https://www.inflearn.com/users/@askcompany)

