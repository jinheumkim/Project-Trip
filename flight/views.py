from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from flight.models import FlightSchedule, Airport, Airline
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
        
        departure_airport_id = Airport.objects.filter(name__icontains=departure_airport).first()
        arrival_airport_id = Airport.objects.filter(name__icontains=arrival_airport).first()
        
        departure_list = []
        arrival_list = []
        
        departure = FlightSchedule.objects.filter(departure_airport = departure_airport_id.id, departure_date = departure_date)
        arrival = FlightSchedule.objects.filter(arrival_airport = arrival_airport_id.id, arrival_date = arrival_date)
        
        
        for search in departure:
            departure_list.append(dict(departure_airport = search.departure_airport,
                                       departure_date = search.departure_date,
                                       arrival_airport = search.arrival_airport,
                                       arrival_date = search.arrival_date,
                                       airline = search.airline,
                                       flight_code = search.flight_code,
                                       departure_time = search.departure_time,
                                       arrival_time = search.arrival_time,
                                       departure_airport_code = departure_airport_id.code,
                                       arrival_airport_code = arrival_airport_id.code,
                                       ))
            
        for search in arrival:
            arrival_list.append(dict(departure_airport = search.departure_airport,
                                       departure_date = search.departure_date,
                                       arrival_airport = search.arrival_airport,
                                       arrival_date = search.arrival_date,
                                       airline = search.airline,
                                       flight_code = search.flight_code,
                                       departure_time = search.departure_time,
                                       arrival_time = search.arrival_time,
                                       departure_airport_code = departure_airport_id.code,
                                       arrival_airport_code = arrival_airport_id.code,))
            
        return render(request, "flight/search.html", context = dict(user=user, email=email,
                                                                    user_login = user_login,
                                                                    departure = departure_list
                                                                    ))
