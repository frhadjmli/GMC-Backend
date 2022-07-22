from django.urls import path
from .views import TempSensorView, HumdSensorView, LuxSensorView, VentilationView, IrrigationView

urlpatterns = [
    path('tempSensor/', TempSensorView.as_view()),
    path('HumdSensor/', HumdSensorView.as_view()),
    path('LuxSensor/', LuxSensorView.as_view()),
    path('Ventilation/', VentilationView.as_view()),
    path('Irrigation/', IrrigationView.as_view()),
]
