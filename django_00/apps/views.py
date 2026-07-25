from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageVeiw(TemplateView):
    template_name = 'home.html'

class AboutPageVeiw(TemplateView):
    template_name = 'about.html'

class MenuPageVeiw(TemplateView):
    template_name = 'menu.html'

class BooksPageVeiw(TemplateView):
    template_name = 'books.html'