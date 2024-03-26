from django.urls import path
from .views import Main, Search

urlpatterns = [
    path('main', Main.as_view()),
    path('search/', Search.as_view()),
]