from django.urls import path
from . import views
from main.views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('host', HostList.as_view()),
    path('event', EventList.as_view()),
    path('drink', DrinkList.as_view()),
    path('food', FoodList.as_view()),
    path('menu', MenuList.as_view()),
]
