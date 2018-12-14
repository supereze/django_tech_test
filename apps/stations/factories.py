# coding: utf8
import factory
from .models import LocationModel,StationModel
from apps.lines.models import LineModel, RouteModel


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LocationModel

    name = factory.Faker('name')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')


class StationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StationModel

    location = factory.SubFactory(LocationFactory)
    order = factory.Faker('order')
    is_active = factory.Faker('is_active')


class LineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LineModel

    name = factory.Faker('name')
    color = factory.Faker('color')


class RouteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RouteModel

    line = factory.SubFactory(LineFactory)
    stations = factory.RelatedFactory(StationFactory, 'location')
    direction = factory.Faker('direction')
    is_active = factory.Faker('is_active')

