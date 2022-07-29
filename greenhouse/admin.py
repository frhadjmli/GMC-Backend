from django.contrib import admin
from .models import (Point, TempSensor, HumdSensor, LuxSensor, 
Irrigation, Ventilation)
# Register your models here.

admin.site.register(Point)
admin.site.register(TempSensor)
admin.site.register(HumdSensor)
admin.site.register(LuxSensor)
admin.site.register(Irrigation)
admin.site.register(Ventilation)