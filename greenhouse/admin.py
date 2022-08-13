from django.contrib import admin
from .models import Point, SensorType, Sensor, SensorValue, DeviceType, Device, DeviceValue, AlarmMessage

admin.site.register(Point)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(SensorValue)
admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(DeviceValue)
admin.site.register(AlarmMessage)