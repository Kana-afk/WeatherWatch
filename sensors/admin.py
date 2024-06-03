from django.contrib import admin
from sensors.models import Sensor, Alert, Data

admin.site.register(Sensor)
admin.site.register(Alert)
admin.site.register(Data)
