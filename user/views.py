from django.shortcuts import render
import os
from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password
from trip.settings import MEDIA_ROOT
from rest_framework.views import APIView

# 이메일, 비밀번호 유효성 검사 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
# Create your views here.

class Join(APIView):
    def get(self, request):
        return render(request,"user/join.html")

    def post(self, request):
        
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)
        
        if User.objects.filter(email = email).exists() == True:
            print('이미 가입된 이메일입니다.')
            return Response('이미 가입된 이메일입니다.', status = 400)
        
        if User.objects.filter(nickname = nickname).exists() == True:
            print('이미 가입된 닉네임입니다.')
            return Response('이미 가입된 닉네임입니다.', status = 400)
            
        
        if email is not None and password is not None:
            try:
                # Validate the email address
                validate_email(email)
                validate_password(password)

                # Create a User object with the validated email
                User.objects.create(email = email, 
                            nickname = nickname,
                            name = name,
                            password = make_password(password),
                            profile_image = "default_profile.png")
                
                return Response(status=200)
            except ValidationError as e:
                print(', '.join(map(str,e)))
                return Response(', '.join(map(str,e)), status=400)
        else:
            return Response(status=400)


class Login(APIView):
    def get(self, request):
        return render(request,"user/login.html")
    
    def post(self, request):
        
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        user = User.objects.filter(email = email).first()
        
        if user is None:
            return Response(status = 400)
        
        if user.check_password(password):
            
            request.session['email'] = email
            return Response(status=200) 
        
        else:
            return Response(status = 400)
        
class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request,"flight/main.html")