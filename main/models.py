from django.db import models
from django.utils import timezone
from django.db.models.fields import CharField, DateField, EmailField, URLField

# Create your models here.

class Host(models.Model):
    host_first_name = models.CharField(max_length=30)
    host_last_name = models.CharField(max_length=30)
    host_address = models.CharField(max_length=30, null=True)
    host_id = models.CharField(max_length=11, null=True)
    host_phone_number = models.CharField(max_length=20, null=True)
    host_email = models.EmailField(null=True)

    def __str__(self):
        return self.host_id

class Event(models.Model):
    event_name = models.CharField(max_length=30)
    event_host = models.ManyToManyField(Host)
    event_responsible_host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='+', null=True)
    event_start_time = models.DateTimeField('Start Time', null=True, default=timezone.now)
    event_end_time = models.DateTimeField('End Time', null=True, default=timezone.now)
    event_address = models.CharField(max_length=30)
    event_place = models.CharField(max_length=30, null=True)
    event_city = models.CharField(max_length=20)
    event_country = models.CharField(max_length=20, null=True)
    event_description = models.TextField()
    event_email = models.EmailField(null=True)
    event_link = models.URLField(null=True)

    def __str__(self):
        return self.event_name

class Drink(models.Model):
    drink_name = models.CharField(max_length=30)
    drink_is_alcoholic = models.BooleanField(default=False)
    drink_price = models.DecimalField(max_digits=6, decimal_places=2)
    drink_amount = models.DecimalField(max_digits=6, decimal_places=2, default='0.03')

    def __str__(self):
        return self.drink_name

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    food_price = models.DecimalField(max_digits=6, decimal_places=2)
    food_is_vege = models.BooleanField(default=False)

    def __str__(self):
        return self.food_name

class Menu(models.Model):
    menu_food = models.OneToOneField(Food, on_delete=models.CASCADE)
    menu_drink = models.OneToOneField(Drink, on_delete=models.CASCADE)

    menu_name = models.CharField(max_length=30)
    menu_is_vege = models.BooleanField(default=False)
    menu_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.menu_name




