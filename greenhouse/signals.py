from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SensorValue, Sensor, DeviceValue, Device
from django.shortcuts import get_object_or_404

from django_eventstream import send_event

@receiver(post_save, sender=SensorValue)
def send_temperature(sender, instance, created, **kwargs):
    if created:
        sensor = get_object_or_404(Sensor, id=instance.sensor_id)
        if sensor.sensor_id[:3] == 'TMP':
            send_event('data_monitoring', 'temp_update', {
                'value': instance.value,
                'id': instance.id,
                'recorded_time': str(instance.recorded_time)
                })
        elif sensor.sensor_id[:3] == 'HUM':
            send_event('data_monitoring', 'humd_update', {
                'value': instance.value,
                'id': instance.id,
                'recorded_time': str(instance.recorded_time)
                })
        elif sensor.sensor_id[:3] == 'LUX':
            send_event('data_monitoring', 'lux_update', {
                'value': instance.value,
                'id': instance.id,
                'recorded_time': str(instance.recorded_time)
                })

@receiver(post_save, sender=DeviceValue)
def send_device_status(sender, instance, created, update_fields, **kwargs):
    
    device = get_object_or_404(Device, id=instance.device_id)
    if device.device_id[:3] == 'FAN':
        send_event('data_controlling', 'fan_status', {
            'status': instance.status,
            'device_ref': instance.device_id
        })
    elif device.device_id[:4] == 'WPMP':
        send_event('data_controlling', 'pump_status', {
            'status': instance.status,
            'device_ref': instance.device_id
        })