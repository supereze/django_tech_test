# coding: utf8
from urbvan_framework.views import ListCreateView, GetPutDeleteView
from .schemas import LocationSchema, StationSchema, LineSchema, RouteSchema
from .serializers import LocationSerializer, StationSerializer, LineSerializer, RouteSerializer
from ..models import LocationModel, StationModel
from apps.lines.models import LineModel, RouteModel


"""CRUD to locations"""


class LocationView(ListCreateView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationEditView(GetPutDeleteView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


"""CRUD to stations"""


class StationView(ListCreateView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationEditView(GetPutDeleteView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


"""CRUD to lines"""


class LineView(ListCreateView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class LineEditView(GetPutDeleteView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


"""CRUD to routes"""


class RouteView(ListCreateView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer


class RouteEditView(GetPutDeleteView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
