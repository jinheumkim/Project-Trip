from django.urls import path
from .views import Main, Search, SaveData, sort_index

urlpatterns = [
    path('main', Main.as_view()),
    path('search/', Search.as_view()),
    path('search_data/', SaveData.as_view()),
    path('sort_index/', sort_index.as_view(), name='sort_index')
]