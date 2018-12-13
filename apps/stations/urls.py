# coding: utf8
from django.urls import path
from .v1 import views as views_v1

urlpatterns_v1_locations = ([
    path('', views_v1.LocationView.as_view(), name='v1_list_create_location'),
    path('create/', views_v1.LocationView.as_view(), name='v1_list_create_location'),
    path('get/', views_v1.LocationView.as_view(), name='v1_list_create_location'),
    path('update/', views_v1.LocationView.as_view(), name='v1_list_create_location'),
    path('delete/', views_v1.LocationView.as_view(), name='v1_list_create_location'),
], 'locations')

urlpatterns_v1_stations = ([
    path('', views_v1.StationView.as_view(), name='v1_list_create_station'),
    path('create/', views_v1.StationView.as_view(), name='v1_list_create_station'),
    path('get/', views_v1.StationView.as_view(), name='v1_list_create_station'),
    path('update/', views_v1.StationView.as_view(), name='v1_list_create_station'),
    path('delete/', views_v1.StationView.as_view(), name='v1_list_create_station'),
], 'stations')

urlpatterns_v1_lines = ([
    path('', views_v1.LineView.as_view(), name='v1_list_create_line'),
    path('create/', views_v1.LineView.as_view(), name='v1_list_create_line'),
    path('get/', views_v1.LineView.as_view(), name='v1_list_create_line'),
    path('update/', views_v1.LineView.as_view(), name='v1_list_create_line'),
    path('delete/', views_v1.LineView.as_view(), name='v1_list_create_line'),
], 'lines')

urlpatterns_v1_routes = ([
    path('', views_v1.RouteView.as_view(), name='v1_list_create_route'),
    path('create/', views_v1.RouteView.as_view(), name='v1_list_create_route'),
    path('get/', views_v1.RouteView.as_view(), name='v1_list_create_route'),
    path('update/', views_v1.RouteView.as_view(), name='v1_list_create_route'),
    path('delete/', views_v1.RouteView.as_view(), name='v1_list_create_route'),
], 'routes')
