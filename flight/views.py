from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from flight.models import FlightSchedule, Airport, Airline, FlightPrice
from trip.settings import MEDIA_ROOT


# Create your views here.

class Main(APIView):
    def get(self, request):
        email = request.session.get('email',None) 
        user = User.objects.filter(email = email).first()
        user_login = User.objects.filter(email = email).exists()
        
        return render(request, "flight/main.html", context = dict(user = user, user_login=user_login))
    
class SaveData(APIView):
    def post(self, request):
        departure_airport = request.data.get('departure_airport')
        arrival_airport = request.data.get('arrival_airport')
        border_count = request.data.get('border_count')
        departure_date = request.data.get('departure_date')
        arrival_date = request.data.get('arrival_date')
        
        departure_flight_code = request.data.get('departure_flight_code')
        
        
        request.session['departure_airport'] = departure_airport
        request.session['arrival_airport'] = arrival_airport
        request.session['border_count'] = border_count
        request.session['departure_date'] = departure_date
        request.session['arrival_date'] = arrival_date
        request.session['departure_flight_code'] = arrival_date
        request.session['departure_flight_code'] = departure_flight_code
        return Response(status=200)
    
class Search(APIView):
    def get(self, request):
        email = request.session.get('email',None)
                    
        user = User.objects.filter(email = email).first()
        user_login = User.objects.filter(email = email).exists()
        
        departure_airport =  request.session.get('departure_airport',None)
        arrival_airport =  request.session.get('arrival_airport',None)
        border_count =  request.session.get('border_count',None)
        departure_date =  request.session.get('departure_date',None)
        arrival_date =  request.session.get('arrival_date',None)
        departure_flight_code = request.session.get('departure_flight_code', None)
        selectedValue = request.session.get('selectedValue',None)
        check_item = request.session.get('check_item',None)
            
        
        
        if selectedValue is None:
            departure_dates = FlightSchedule.objects.filter(departure_date__icontains = departure_date).order_by('flight_prices__price')
            arrival_dates = FlightSchedule.objects.filter(arrival_date__icontains = arrival_date).order_by('flight_prices__price')
                
        elif selectedValue == "price":
            departure_dates = FlightSchedule.objects.filter(departure_date__icontains = departure_date).order_by('flight_prices__price')
            arrival_dates = FlightSchedule.objects.filter(arrival_date__icontains = arrival_date).order_by('flight_prices__price')

        
            
        elif selectedValue == "time_asc":
            departure_dates = FlightSchedule.objects.filter(departure_date__icontains = departure_date).order_by('departure_time')
            arrival_dates = FlightSchedule.objects.filter(arrival_date__icontains = arrival_date).order_by('departure_time')
            
        elif selectedValue == "time_desc":
            departure_dates = FlightSchedule.objects.filter(departure_date__icontains = departure_date).order_by('-departure_time')
            arrival_dates = FlightSchedule.objects.filter(arrival_date__icontains = arrival_date).order_by('-departure_time')
            
        
        
        departure_count = FlightSchedule.objects.filter(departure_date__icontains = departure_date).count()
        arrival_count = FlightSchedule.objects.filter(arrival_date__icontains = arrival_date).count()
        
        departure_select = FlightSchedule.objects.filter(flight_code = departure_flight_code)
        departure_selecting = FlightSchedule.objects.filter(flight_code = departure_flight_code).exists()
         
            
        departure_select_list = []
        
        if departure_select is not None:
            for select in departure_select:
                price = FlightPrice.objects.filter(flight_schedule = select.id).first().price
                departure_select_list.append(dict(id = select.id,
                                                  flight_code = select.flight_code,
                                                  departure_time = select.departure_time,
                                                  departure_airport = select.departure_airport,
                                                  departure_date = select.departure_date,
                                                  arrival_time = select.arrival_time,
                                                  arrival_airport = select.arrival_airport,
                                                  airline_image = select.airline.image,
                                                  departure_airport_code = select.departure_airport.code,
                                                  arrival_airport_code = select.arrival_airport.code,
                                                  price= price
                                                  ))
                
                
        arrival_list = []
        if departure_selecting == True:
            for arrival in arrival_dates:
                price = FlightPrice.objects.filter(flight_schedule = arrival.id).first().price
                arrival_list.append(dict(flight_code = arrival.flight_code,
                                    id = arrival.id,
                                    departure_time = arrival.departure_time,
                                    airline = arrival.airline,
                                    arrival_airport = arrival.arrival_airport,
                                    arrival_date = arrival.arrival_date,
                                    arrival_time = arrival.arrival_time,
                                    departure_airport = arrival.departure_airport,
                                    price = price
                                    ))
        
        departure_list = []
        for departure in departure_dates:
            price = FlightPrice.objects.filter(flight_schedule = departure.id).first().price
            departure_list.append(dict(flight_code = departure.flight_code,
                                    id = departure.id,
                                    departure_time = departure.departure_time,
                                    airline = departure.airline,
                                    departure_airport = departure.departure_airport,
                                    departure_date = departure.departure_date,
                                    arrival_time = departure.arrival_time,
                                    arrival_airport = departure.arrival_airport,
                                    price = price
                                    ))
            
        
        
        return render(request, 'flight/search.html',context = dict(departure_airport = departure_airport,
                                                                   arrival_airport = arrival_airport,
                                                                   border_count = border_count,
                                                                   departure_date = departure_date,
                                                                   arrival_date = arrival_date,
                                                                   user = user, user_login = user_login,
                                                                   departures = departure_list,
                                                                   departure_count = departure_count,
                                                                   departure_select = departure_select_list,
                                                                   departure_selecting = departure_selecting,
                                                                   arrivals = arrival_list,
                                                                   arrival_count = arrival_count
                                                                   ))


class sort_index(APIView):
    def post(self,request):
        selectedValue = request.data.get('selectedValue')
        request.session['selectedValue'] = selectedValue
        return Response(status=200)
    
    
class check_airline(APIView):
    def post(self,request):
        check_item = request.POST.getlist('check_item[]')
        request.session['check_item'] = check_item
        return Response(status=200)