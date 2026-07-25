from django.urls import path
from .views import HomePageVeiw, AboutPageVeiw, MenuPageVeiw, BooksPageVeiw

urlpatterns = [
    path('', HomePageVeiw.as_view(), name = "home"),
    path('about/', AboutPageVeiw.as_view(), name = "about"),
    path('menu/', MenuPageVeiw.as_view(), name = "menu"),
    path('books/', BooksPageVeiw.as_view(), name = "books"),
]