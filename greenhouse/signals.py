from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SensorValue, Sensor, AlarmMessage, DeviceValue, Device
from django.shortcuts import get_object_or_404
from django_eventstream import send_event
from . utils import detect_alarm, retrive_renge_val, get_extra_data_from_alarm_message


@receiver(post_save, sender=SensorValue)
def send_data_sensor_value(sender, instance, created, **kwargs):
    if created:
        sensor = get_object_or_404(Sensor, id=instance.sensor_id)
        range_value = retrive_renge_val()
        if sensor.sensor_id[:3] == 'TMP':
            send_event('data_monitoring', 'temp_update', {
                'value': instance.value,
                'id': instance.id,
                'recorded_time': str(instance.recorded_time)
                })
            detect_alarm(range_value['Temperature'], instance, message="دما ")

        elif sensor.sensor_id[:3] == 'HUM':
            send_event('data_monitoring', 'humd_update', {
                'value': instance.value,
                'id': instance.id,
                'recorded_time': str(instance.recorded_time)
                })
            detect_alarm(range_value['Humidity'], instance, message="رطوبت ")

        elif sensor.sensor_id[:3] == 'LUX':
            send_event('data_monitoring', 'lux_update', {
                'value': instance.value,
                'id': instance.id,
                'recorded_time': str(instance.recorded_time)
                })
            detect_alarm(range_value['Lux'], instance, message="شدت نور ")


@receiver(post_save, sender=AlarmMessage)
def send_alarm(sender, instance, created, **kwargs):
    if created:
        data = get_extra_data_from_alarm_message(instance.id)
        sensor_id = data['sensor_id']
        if sensor_id[:3] == 'TMP':
            send_event('data_monitoring', 'temp_alarm', {
                'id': instance.id,
                'body_text': instance.body_text,
                'recorded_time': str(data['recorded_time']),
                'date_time': str(data['date_time'])
                })
        elif sensor_id[:3] == 'HUM':
            send_event('data_monitoring', 'humd_alarm', {
                'id': instance.id,
                'body_text': instance.body_text,
                'recorded_time': str(data['recorded_time']),
                'date_time': str(data['date_time'])
                })
        elif sensor_id[:3] == 'LUX':
            send_event('data_monitoring', 'lux_alarm', {
                'id': instance.id,
                'body_text': instance.body_text,
                'recorded_time': str(data['recorded_time']),
                'date_time': str(data['date_time'])
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
