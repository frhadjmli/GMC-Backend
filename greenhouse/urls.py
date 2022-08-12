from django.urls import path
from .views import TempSensorView, HumidSensorView, LuxSensorView, VentilationView, IrrigationView
from .views import SensorView, SensorValueView

urlpatterns = [
    path('sensor/', SensorView.as_view()),
    path('sensorValue/', SensorValueView.as_view()),

    path('tempSensor/', TempSensorView.as_view()),
    path('HumdSensor/', HumidSensorView.as_view()),
    path('LuxSensor/', LuxSensorView.as_view()),
    path('Ventilation/', VentilationView.as_view()),
    path('Ventilation/update/<int:device_id>/', VentilationView.as_view()),
    path('Irrigation/', IrrigationView.as_view()),
    path('Irrigation/update/<int:device_id>/', IrrigationView.as_view()),
 ]
