from django.db import models

# Create your models here.

class FlightSchedule(models.Model):
    flight_code = models.CharField(max_length = 45) ##항공편명
    departure_date = models.CharField(max_length = 10) ##출발 날짜
    arrival_date = models.CharField(max_length = 10) ##도착 날짜
    departure_time = models.TimeField() ##출발 시각
    arrival_time = models.TimeField()  ##도착 시각
    departure_airport = models.ForeignKey('Airport', related_name='departure_airport', on_delete=models.CASCADE) ##출발 공항
    arrival_airport = models.ForeignKey('Airport', related_name='arrival_airport', on_delete=models.CASCADE) ##도착 공항
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE) ##항공사
    
    class Meta:
        db_table = 'flight_schedules'
        
class Airline(models.Model): ##항공사 
    name = models.CharField(max_length = 300) 
    image = models.TextField()
    
    class Meta:
        db_table = 'airlines'

class Airport(models.Model): ##공항
    name = models.CharField(max_length=400)
    code = models.CharField(max_length=10)

    class Meta:
        db_table = 'airports'
        
class FlightPrice(models.Model): 
    price           = models.IntegerField() ##가격
    remaining_seat  = models.IntegerField() ## 남은 좌석
    flight_schedule = models.ForeignKey('FlightSchedule', on_delete=models.CASCADE, related_name='flight_prices') ##항공 스케쥴 아이디
    status          = models.ForeignKey('FlightStatus', on_delete=models.CASCADE, default=1)  ## 상태

    class Meta:
        db_table = 'flight_prices'
        
class FlightStatus(models.Model):  ## 상태
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'flight_statuses'