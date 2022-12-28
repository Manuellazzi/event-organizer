import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *

NUM_HOSTS = 100
NUM_EVENTS = 100
NUM_DRINKS = 100
NUM_FOODS = 100
NUM_MENUS = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Host, Event, Drink, Food, Menu]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_EVENTS):
            event = EventFactory()

        for _ in range(NUM_HOSTS):
            host = HostFactory()
        
        for _ in range(NUM_DRINKS):
            drink = DrinkFactory()

        for _ in range(NUM_FOODS):
            food = FoodFactory()

        for _ in range(NUM_MENUS):
            menu = MenuFactory()
