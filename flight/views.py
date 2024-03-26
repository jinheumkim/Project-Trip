from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from flight.models import FlightSchedule, Airport
from trip.settings import MEDIA_ROOT


# Create your views here.

class Main(APIView):
    def get(self, request):
        email = request.session.get('email',None) 
        user = User.objects.filter(email = email).first()
        user_login = User.objects.filter(email = email).exists()
        
        return render(request, "flight/main.html", context = dict(user = user, user_login=user_login))
    


class Search(APIView):
    def get(self, request):
            
        email = request.session.get('email',None)
            
        # departure_airport = request.data.get('departure_airport', None)
        # arrival_airport = request.data.get('arrival_airport', None)
        # border_count = request.data.get('border_count', None)
        # departure_date = request.data.get('departure_date' ,None)
        # arrival_date = request.data.get('arrival_date', None)
            
                    
        user = User.objects.filter(email = email).first()
        user_login = User.objects.filter(email = email).exists()
        
        
        departure_airport = request.GET.get('key1')
        arrival_airport = request.GET.get('key2')
        departure_date = request.GET.get('key3')
        arrival_date = request.GET.get('key4')
        border_count = request.GET.get('key5')
        
        flight_search_object = FlightSchedule.objects.all()
        flight_search = []
        for search in flight_search_object:
            print(search)
            
        if departure_airport:
            departure_airport = Airport.objects.filter(name__icontains=departure_airport)
        if arrival_airport:
            arrival_airport = Airport.objects.filter(name__icontains=arrival_airport)
        if departure_date:
            departure_date = FlightSchedule.objects.filter(departure_date__icontains=departure_date)
            print(departure_date)
        if arrival_date:
            arrival_date = FlightSchedule.objects.filter(arrival_date__icontains=arrival_date)
        
        
    
        return render(request, "flight/search.html", context = dict(user=user, email=email,
                                                                    ))
