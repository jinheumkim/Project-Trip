from django.urls import path
from .views import Main, Search, SaveData, sort_index, check_airline

urlpatterns = [
    path('main', Main.as_view()),
    path('search/', Search.as_view()),
    path('search_data/', SaveData.as_view()),
    path('sort_index/', sort_index.as_view(), name='sort_index'),
    path('check_airline/', check_airline.as_view(), name='check_airline'),
]