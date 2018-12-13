from django.contrib import admin
from .models import LocationModel, StationModel

admin.site.register(LocationModel)
admin.site.register(StationModel)