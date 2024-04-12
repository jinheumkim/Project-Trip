from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from flight.models import FlightSchedule
# Create your models here.

class User(AbstractBaseUser):
    
    profile_image = models.TextField()
    nickname = models.CharField(max_length = 24, unique = True)
    name = models.CharField(max_length = 12)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 24)
    
    USERNAME_FIELD = 'nickname'
    
    class Meta :
        db_table = "User"
        
        
        
class Reservation(models.Model):
    
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user', default= '')
    departure_reservation = models.ForeignKey("flight.FlightSchedule", related_name='departure_reservation', on_delete=models.CASCADE, default = '')
    arrival_reservation = models.ForeignKey("flight.FlightSchedule", related_name='arrival_reservation', on_delete=models.CASCADE, default = '')
    
    class Meta :
        db_table = "Reservation"