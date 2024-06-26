from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User, Reservation
from flight.models import FlightSchedule, Airport, Airline, FlightPrice, FlightStatus
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
        arrival_flight_code = request.data.get('arrival_flight_code')
        
        
        
        
        request.session['departure_airport'] = departure_airport
        request.session['arrival_airport'] = arrival_airport
        request.session['border_count'] = border_count
        request.session['departure_date'] = departure_date
        request.session['arrival_date'] = arrival_date
        request.session['departure_flight_code'] = arrival_date
        request.session['departure_flight_code'] = departure_flight_code
        request.session['arrival_flight_code'] = arrival_flight_code
        
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
        arrival_flight_code = request.session.get('arrival_flight_code',None)
        
        
        try:
            departure_airport_id = Airport.objects.filter(name = departure_airport).first().id
            arrival_airport_id = Airport.objects.filter(name = arrival_airport).first().id
        except AttributeError :
            return render(request, 'flight/search.html', context =dict(departure_airport = departure_airport,
                                                                   arrival_airport = arrival_airport,
                                                                   border_count = border_count,
                                                                   departure_date = departure_date,
                                                                   arrival_date = arrival_date,
                                                                   user = user, user_login = user_login,
                                                                   ) )
        

        
        
        if selectedValue is None:
            departure_dates = FlightSchedule.objects.filter(departure_date = departure_date, departure_airport = departure_airport_id, arrival_airport = arrival_airport_id).order_by('flight_prices__price')
            arrival_dates = FlightSchedule.objects.filter(arrival_date = arrival_date, departure_airport = arrival_airport_id, arrival_airport = departure_airport_id).order_by('flight_prices__price')
                
        elif selectedValue == "price":
            departure_dates = FlightSchedule.objects.filter(departure_date = departure_date, departure_airport = departure_airport_id, arrival_airport = arrival_airport_id).order_by('flight_prices__price')
            arrival_dates = FlightSchedule.objects.filter(arrival_date = arrival_date, departure_airport = arrival_airport_id, arrival_airport = departure_airport_id).order_by('flight_prices__price')
            
        elif selectedValue == "time_asc":
            departure_dates = FlightSchedule.objects.filter(departure_date = departure_date, departure_airport = departure_airport_id, arrival_airport = arrival_airport_id).order_by('departure_time')
            arrival_dates = FlightSchedule.objects.filter(arrival_date = arrival_date, departure_airport = arrival_airport_id, arrival_airport = departure_airport_id).order_by('departure_time')
            
        elif selectedValue == "time_desc":
            departure_dates = FlightSchedule.objects.filter(departure_date = departure_date, departure_airport = departure_airport_id, arrival_airport = arrival_airport_id).order_by('-departure_time')
            arrival_dates = FlightSchedule.objects.filter(arrival_date = arrival_date, departure_airport = arrival_airport_id, arrival_airport = departure_airport_id).order_by('-departure_time')
        
        
        departure_count = FlightSchedule.objects.filter(departure_date = departure_date,departure_airport = departure_airport_id, arrival_airport = arrival_airport_id).count()
        arrival_count = FlightSchedule.objects.filter(arrival_date = arrival_date, departure_airport = arrival_airport_id, arrival_airport = departure_airport_id).count()
        
        departure_select = FlightSchedule.objects.filter(flight_code = departure_flight_code)
        departure_selecting = FlightSchedule.objects.filter(flight_code = departure_flight_code).exists()
        
        arrival_select_list = []
        arrival_select = FlightSchedule.objects.filter(flight_code = arrival_flight_code)
        arrival_selecting = FlightSchedule.objects.filter(flight_code = arrival_flight_code).exists()
        
        
        if arrival_select is not None:
            for select in arrival_select:
                price = FlightPrice.objects.filter(flight_schedule = select.id).first().price
                remaining_seat = FlightPrice.objects.filter(flight_schedule = select.id).first().remaining_seat
                arrival_select_list.append(dict(id = select.id,
                                                  flight_code = select.flight_code,
                                                  departure_time = select.departure_time,
                                                  departure_airport = select.departure_airport,
                                                  departure_date = select.departure_date,
                                                  arrival_time = select.arrival_time,
                                                  arrival_airport = select.arrival_airport,
                                                  airline_image = select.airline.image,
                                                  departure_airport_code = select.departure_airport.code,
                                                  arrival_airport_code = select.arrival_airport.code,
                                                  airline_name = select.airline.name,
                                                  price= price,
                                                  remaining_seat = remaining_seat
                                                  ))
         
            
        departure_select_list = []
        
        if departure_select is not None:
            for select in departure_select:
                price = FlightPrice.objects.filter(flight_schedule = select.id).first().price
                remaining_seat = FlightPrice.objects.filter(flight_schedule = select.id).first().remaining_seat
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
                                                  airline_name = select.airline.name,
                                                  price= price,
                                                  remaining_seat = remaining_seat
                                                  ))
        
    
                
        
        arrival_list = []
        if departure_selecting == True:
            for arrival in arrival_dates:
                price = FlightPrice.objects.filter(flight_schedule = arrival.id).first().price
                remaining_seat = FlightPrice.objects.filter(flight_schedule = arrival.id).first().remaining_seat
                arrival_list.append(dict(flight_code = arrival.flight_code,
                                    id = arrival.id,
                                    departure_time = arrival.departure_time,
                                    airline = arrival.airline,
                                    arrival_airport = arrival.arrival_airport,
                                    arrival_date = arrival.arrival_date,
                                    arrival_time = arrival.arrival_time,
                                    departure_airport = arrival.departure_airport,
                                    price = price,
                                    remaining_seat = remaining_seat
                                    ))
        
        departure_list = []
        for departure in departure_dates:
            price = FlightPrice.objects.filter(flight_schedule = departure.id).first().price
            remaining_seat = FlightPrice.objects.filter(flight_schedule = departure.id).first().remaining_seat
            departure_list.append(dict(flight_code = departure.flight_code,
                                    id = departure.id,
                                    departure_time = departure.departure_time,
                                    airline = departure.airline,
                                    departure_airport = departure.departure_airport,
                                    departure_date = departure.departure_date,
                                    arrival_time = departure.arrival_time,
                                    arrival_airport = departure.arrival_airport,
                                    price = price,
                                    remaining_seat = remaining_seat
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
                                                                   arrival_count = arrival_count,
                                                                   arrival_select = arrival_select_list,
                                                                   arrival_select_list = arrival_select,
                                                                   arrival_selecting = arrival_selecting
                                                                   ))

class Sort_index(APIView):
    def post(self,request):
        selectedValue = request.data.get('selectedValue')
        request.session['selectedValue'] = selectedValue
        return Response(status=200)

class Reservation_create(APIView):
    def get(self, request):
        email = request.session.get('email',None)
                    
        user = User.objects.filter(email = email).first()
        user_login = User.objects.filter(email = email).exists()
        return render(request, 'flight/reservation.html', context = dict(user = user, user_login = user_login))
        
    def post(self, request):
        email = request.session.get('email',None)
                    
        user = User.objects.filter(email = email).first()
        
        departure_reservation = request.data.get('departure_reservation')
        arrival_reservation = request.data.get('arrival_reservation')
        
        departure_reservation = FlightSchedule.objects.filter(flight_code = departure_reservation).first()
        arrival_reservation = FlightSchedule.objects.filter(flight_code = arrival_reservation).first()
        
        Reservation.objects.create(user_id = user.id ,departure_reservation_id = departure_reservation.id, arrival_reservation_id = arrival_reservation.id)
        
        return Response(status=200)
    
    
