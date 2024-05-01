# Project-Trip

### 기술 스택
----------------------
Python, Django, Jquery, css
### 프로젝트 설명
----------------------
항공권 예약 사이트 만들어보기
### 프로젝트 구조
----------------------
Project
 * Trip
Apps
 * flight
 * user


### ERD
-------------------

### 구현 기능
--------------------
#### 로그인

* 사이트 접속 시 로그인 창 및 회원가입과 로그인 구현
  
* 로그아웃 구현

* 회원가입 시 make_password를 사용하여 패스워드 암호화
* 회원 가입 시 validate_email을 사용하여 email 형식에 맞지 않을 시 에러 반환
  
* 회원 가입 시validate_password를 사용하여 비밀번호가
  8자리 이상, 반복되는 비밀번호, 숫자/영어/특수문자 중 2가지 이상 포함되지 않을 시 에러 반환



#### 메인 화면

* 모달창을 이용하여 출발지, 도착지 선택하기
  
![출발 도착지 선택](https://github.com/jinheumkim/Project-Trip/assets/126999253/f276998d-83ba-42ed-91be-771605b8f5a5)

* 출발지 도착지 value값 바꾸기
  
![출발지 도착지 value변경](https://github.com/jinheumkim/Project-Trip/assets/126999253/7e39b589-69fc-4b47-a727-8916ef07db5f)

* DatePicker사용하여 날짜 선택하기, 지나간 날짜는 선택 불가능으로 표시

![날짜 선택](https://github.com/jinheumkim/Project-Trip/assets/126999253/73ed3938-5410-4b1b-a5a6-7f5588e73a10)

* 모달 창을 이용하여 탑승객 수를 카운트
  
![인원선택](https://github.com/jinheumkim/Project-Trip/assets/126999253/7a27735c-86da-4563-bdbd-0b1a526326d4)

* 키워드 선택 안했을 시 alert창, 모두 선택 시 항공권 검색 기능
  
![alert창](https://github.com/jinheumkim/Project-Trip/assets/126999253/9123786b-4f8a-466e-b568-0989a8f1b8b0)


#### 항공권 검색완료 화면

* 선택한 키워드에 따른 항공편만 표시

  ![검색 완료](https://github.com/jinheumkim/Project-Trip/assets/126999253/0b1a5740-f102-4334-9412-07a9b7169591)


* 검색된 항공편을 가격 낮은 순, 출발 시간 빠른 순, 출발 시간 느린 순으로 정렬하는 기능 구현

  ![정렬하기](https://github.com/jinheumkim/Project-Trip/assets/126999253/f14f32d8-b470-4a38-b1af-84451fc2e131)

  
* 항공권 선택 시 선택된 항공편을 보여주고 변경 가능

  ![출발지 선택 변경하기](https://github.com/jinheumkim/Project-Trip/assets/126999253/fcb3c99f-5c3b-41fa-81d8-e30098f9ba84)


* 출발, 도착 항공편을 모두 선택 시 상세요금표 보여주기


![도착지 선택](https://github.com/jinheumkim/Project-Trip/assets/126999253/e7410831-a271-4345-a844-8f6efb269091)
  
* 예약 인원에 따른 요금 적용, 예약하기 구현
  
![예약 완료](https://github.com/jinheumkim/Project-Trip/assets/126999253/df2864d3-857e-43e9-b86d-234440d2b417)




### Aws로 ubuntu 서버 사용
* putty 사용
* nginx/uwsgi 사용하여 상시로 서버 띄워놓기
* docker 사용, mysql image 사용하여 mysql 연동
* vscode Database Client JDBC로 mysql database를 vscode로 연동
* ubuntu 서버의 uwsgi.ini에 database 정보 os.environ.get으로 숨겨두기
* settings_local.py로 메인서버에 개입하지 않고 python manage.py runserver --settings=insta.settings_local로 로컬서버 접속하여 테스트 가능

### settings.py database 정보 및 Actions 정보
--------------------
#### settings
DATABASES = {
    
    'default': {
        
        'ENGINE': 'django.db.backends.mysql',
        
        'NAME': 'insta',
        
        'HOST' : os.environ.get,
        
        'USER' : os.environ.get,
        
        'PASSWORD' : os.environ.get,
        
        'PORT' :'3306',
    
        'OPTIONS' : {'charset' : 'utf8mb4'},

    }

}
#### Actions
  host : ${{ secrets.HOST }}
  
  username : ${{ secrets.USERNAME }}
  
  key : ${{secrets.KEY}}

  port : 22
