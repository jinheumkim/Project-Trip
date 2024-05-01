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

* 출발지, 도착지를 클릭하여 검색 준비하기


* 출발지 도착지 value값 바꾸기
  

* DatePicker사용하여 날짜 선택하기, 지나간 날짜는 선택 불가능으로 표시
  

* 모달 창을 이용하여 탑승객 수를 카운트
  

* 키워드 선택 안했을 시 alert창, 모두 선택 시 항공권 검색 기능
  


#### 항공권 검색완료 화면

* 선택한 키워드에 따른 항공편만 표시


* 검색된 항공편을 가격 낮은 순, 출발 시간 빠른 순, 출발 시간 느린 순으로 정렬하는 기능 구현

  
* 항공권 선택 시 선택된 항공편을 보여주고 변경 가능


* 출발, 도착 항공편을 모두 선택 시 상세요금표 보여주기

  
* 예약 인원에 따른 요금 적용, 예약하기 구현




### Aws로 ubuntu 서버 사용
* putty 사용
* nginx/uwsgi 사용하여 상시로 서버 띄워놓기
* docker 사용, mysql image 사용하여 mysql 연동
* vscode Database Client JDBC로 mysql database를 vscode로 연동
* ubuntu 서버의 uwsgi.ini에 database 정보 os.environ.get으로 숨겨두기
* settings_local.py로 메인서버에 개입하지 않고 python manage.py runserver --settings=insta.settings_local로 로컬서버 접속하여 테스트 가능

### Git Actions
---------------------
##### * Django CI로 VSCODE COMMIT시 파이썬 3.8 3.9버전으로 회원가입과 로그인 테스트 후 성공시 CD 진행시키기 자동화
##### * Django CD로 aws cloud 서비스로 띄워놓은 ubuntu 서버 접속 후
##### * cd /home/ubuntu/insta-ec2 ---> git pull ---> sudo systemctl restart uwsgi로 nginx/uwsgi로 상시 띄워놓은 서버에 자동 적용시키기

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
