## factory.py
import factory
from factory.django import DjangoModelFactory
from main.models import *
import factory.fuzzy
from django.utils import timezone

## Defining a factory
class HostFactory(DjangoModelFactory): 
    class Meta:
        model = Host

    host_first_name = factory.Faker("first_name")
    host_last_name = factory.Faker("last_name")
    host_address = factory.Faker("address")
    host_id = factory.Faker('pyint', min_value=10000000000, max_value=99999999999)
    host_phone_number = factory.Faker("phone_number")
    host_email = factory.Faker("email")


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    event_name = factory.Faker("name")       
    event_responsible_host = factory.SubFactory(HostFactory)
    event_start_time = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    event_end_time = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    event_address = factory.Faker("street_address")
    event_place = factory.Faker("name")
    event_city = factory.Faker("city")
    event_country = factory.Faker("country")
    event_description = factory.Faker("paragraph", nb_sentences=10)
    event_email = factory.Faker("email")
    event_link = factory.Faker("url")

    @factory.post_generation
    def event_host(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for host in extracted:
                self.event_host.add(host)


class DrinkFactory(DjangoModelFactory):
    class Meta:
        model = Drink

    drink_name = factory.Faker("name")
    drink_is_alcoholic = factory.Faker("pybool")
    drink_price = factory.fuzzy.FuzzyDecimal(low=1, high=10000, precision=2)
    drink_amount = factory.fuzzy.FuzzyDecimal(low=0, high=1, precision=2)


class FoodFactory(DjangoModelFactory):
    class Meta:
        model = Food

    food_name = factory.Faker("name")
    food_price = factory.fuzzy.FuzzyDecimal(low=1, high=10000, precision=2)
    food_is_vege = factory.Faker("pybool")


class MenuFactory(DjangoModelFactory):
    class Meta:
        model = Menu

    menu_food = factory.Iterator(Food.objects.all())
    menu_drink = factory.Iterator(Drink.objects.all())

    menu_name = factory.Faker("name")
    menu_is_vege = factory.Faker("pybool")
    menu_price = factory.fuzzy.FuzzyDecimal(low=1, high=10000, precision=2)