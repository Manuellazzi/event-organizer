from django.views.generic import ListView
from main.models import *
from django.shortcuts import render
from django.http import HttpResponse

## Create your views here.
def homepage(request):
    return render(request, 'base_generic.html')

class HostList(ListView):
    model = Host

class EventList(ListView):
    model = Event

class DrinkList(ListView):
    model = Drink

class FoodList(ListView):
    model = Food

class MenuList(ListView):
    model = Menu
