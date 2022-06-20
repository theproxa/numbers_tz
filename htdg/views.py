from django.shortcuts import render
from requests import request

# Create your views here.
from .models import Orders
from django.views.generic import ListView
from .GoogleSheetsApi import add_db

class HomeView(ListView):
    model=Orders
    add_db()
    template_name = 'home.html'
    