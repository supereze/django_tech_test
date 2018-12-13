# coding: utf8
from urbvan_framework.views import ListCreateView
from .schemas import LocationSchema, StationSchema, LineSchema, RouteSchema
from .serializers import LocationSerializer, StationSerializer, LineSerializer, RouteSerializer
from ..models import LocationModel, StationModel
from apps.lines.models import LineModel, RouteModel


class LocationView(ListCreateView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class StationView(ListCreateView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class LineView(ListCreateView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class RouteView(ListCreateView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
