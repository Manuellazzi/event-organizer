from multiprocessing import Event
from django.contrib import admin
from .models import *

## Register your models here.
model_list = [Event, Host, Drink, Food, Menu]
admin.site.register(model_list)
