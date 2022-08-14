from django.urls import path
# from .views import TempSensorView, HumidSensorView, LuxSensorView, VentilationView, IrrigationView
# from .views import SensorView, SensorValueView
from .views import SensorValueInfoView, DeviceValueInfoView

urlpatterns = [
    # path('sensor/', SensorView.as_view()),
    # path('sensorValue/', SensorValueView.as_view()),

    path('SensorValueInfo/<int:sensor_type_id>/', SensorValueInfoView.as_view()),
    path('SensorValueInfo/', SensorValueInfoView.as_view()),

    # path('HumdSensor/', HumidSensorView.as_view()),
    # path('LuxSensor/', LuxSensorView.as_view()),
    path('DeviceValueInfo/<int:device_type_id>/', DeviceValueInfoView.as_view()),
    path('DeviceValueInfo/update/<int:device_id>/', DeviceValueInfoView.as_view()),
    # path('Irrigation/', IrrigationView.as_view()),
    # path('Irrigation/update/<int:device_id>/', IrrigationView.as_view()),
 ]
