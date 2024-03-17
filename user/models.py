from django.db import models
from django.contrib.auth.models import AbstractBaseUser
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