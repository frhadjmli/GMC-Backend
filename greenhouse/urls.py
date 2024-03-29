from django.urls import path
from .views import SensorValueInfoView, DeviceValueInfoView, AlarmMessageView, AlarmMessageIsSeenView, \
    CountSensorDeviceView, SensorTypeRangeView

urlpatterns = [
    path('SensorValueInfo/<int:sensor_type_id>/', SensorValueInfoView.as_view()),
    path('SensorValueInfo/', SensorValueInfoView.as_view()),

    path('DeviceValueInfo/<int:device_type_id>/', DeviceValueInfoView.as_view()),
    path('DeviceValueInfo/update/<int:device_id>/', DeviceValueInfoView.as_view()),

    path('AlarmMessage/', AlarmMessageView.as_view()),
    path('AlarmMessage/update/', AlarmMessageView.as_view()),
    path('AlarmMessage/notSeen/', AlarmMessageIsSeenView.as_view()),

    path('CountSensorDevice/', CountSensorDeviceView.as_view()),

    path('SensorTypeRange/', SensorTypeRangeView.as_view()),
    path('SensorTypeRange/update/<int:sensor_type_range_id>/', SensorTypeRangeView.as_view()),

 ]
