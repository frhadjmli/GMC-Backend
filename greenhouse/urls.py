from django.urls import path
from .views import TempSensorView

urlpatterns = [
    path('tempSensor/', TempSensorView.as_view()),
]
