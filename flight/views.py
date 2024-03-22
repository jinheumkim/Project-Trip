from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from trip.settings import MEDIA_ROOT

# Create your views here.

class Main(APIView):
    def get(self, request):
        email = request.session.get('email',None) 
        user = User.objects.filter(email = email).first()
        user_login = User.objects.filter(email = email).exists()
        
        return render(request, "flight/main.html", context = dict(user = user, user_login=user_login))
    
class Search_flight(APIView):
    def get(self,request):
        email = request.session.get('email',None) 
        user = User.objects.filter(email = email).first()
        user_login = User.objects.filter(email = email).exists()
        
        return render(request, "flight/search.html", context = dict(user = user, user_login = user_login))