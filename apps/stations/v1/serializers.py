# coding: utf8
from rest_framework import serializers
from apps.stations.models import LocationModel, StationModel
from apps.lines.models import LineModel, RouteModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StationModel
        exclude = ('id', )


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineModel
        exclude = ('id', )


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouteModel
        exclude = ('id', )
