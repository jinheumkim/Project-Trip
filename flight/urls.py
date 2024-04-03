from django.urls import path
from .views import Main, Search, SaveData

urlpatterns = [
    path('main', Main.as_view()),
    path('search/', Search.as_view()),
    path('search_data/', SaveData.as_view())
]