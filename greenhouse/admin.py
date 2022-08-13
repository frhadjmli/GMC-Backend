from django.contrib import admin
# from .models import (Point, TempSensor, HumdSensor, LuxSensor,
# Irrigation, Ventilation)
from .models import Point, Sensor_type, Sensor, Sensor_value, Device_type, Device, Device_value, Alarm_message

# admin.site.register(Point)
# admin.site.register(TempSensor)
# admin.site.register(HumdSensor)
# admin.site.register(LuxSensor)
# admin.site.register(Irrigation)
# admin.site.register(Ventilation)

admin.site.register(Point)
admin.site.register(Sensor_type)
admin.site.register(Sensor)
admin.site.register(Sensor_value)
admin.site.register(Device_type)
admin.site.register(Device)
admin.site.register(Device_value)
admin.site.register(Alarm_message)