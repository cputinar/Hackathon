from django.contrib import admin
from phLow.models import Device
from phLow.models import DeviceType
from phLow.models import Plant
from phLow.models import Sensor
from phLow.models import Zone

# Register your models here.
admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(Plant)
admin.site.register(Sensor)
admin.site.register(Zone)
