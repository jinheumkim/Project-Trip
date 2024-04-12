from django.urls import path
from .views import Main, Search, SaveData, Sort_index,Reservation_create

urlpatterns = [
    path('main', Main.as_view()),
    path('search/', Search.as_view()),
    path('search_data/', SaveData.as_view()),
    path('sort_index/', Sort_index.as_view(),),
    path('reservation/', Reservation_create.as_view()),
]