from django.urls import path
from .views import Main,Search_flight

urlpatterns = [
    path('main', Main.as_view()),
    path('search', Search_flight.as_view()),
    
]
