# coding: utf8
from django.urls import path
from .v1 import views as views_v1

urlpatterns_v1_locations = ([
    path('', views_v1.LocationView.as_view(), name='v1_list_create_location'),
    path('<pk>/', views_v1.LocationEditView.as_view(), name='v1_get_put_delete_location'),
], 'locations')

urlpatterns_v1_stations = ([
    path('', views_v1.StationView.as_view(), name='v1_list_create_station'),
    path('<pk>/', views_v1.StationEditView.as_view(), name='v1_get_put_delete_station'),
], 'stations')

urlpatterns_v1_lines = ([
    path('', views_v1.LineView.as_view(), name='v1_list_create_line'),
    path('<pk>/', views_v1.LineEditView.as_view(), name='v1_get_put_delete_line'),
], 'lines')

urlpatterns_v1_routes = ([
    path('', views_v1.RouteView.as_view(), name='v1_list_create_route'),
    path('<pk>/', views_v1.RouteEditView.as_view(), name='v1_get_put_delete_route'),
], 'routes')
