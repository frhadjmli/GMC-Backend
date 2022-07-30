import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_eventstream import send_event

from .models import TempSensor, HumdSensor, LuxSensor


@receiver(post_save, sender=TempSensor)
def send_temperature(sender, instance, created, **kwargs):
    if created:
        send_event('data_monitoring', 'temp_update', {
            'temp_value': instance.temp_value,
            'id': instance.id,
            'recorded_time': str(instance.recorded_time)
            })

@receiver(post_save, sender=HumdSensor)
def send_humidity(sender, instance, created, **kwargs):
    if created:
        send_event('data_monitoring', 'humd_update', {
            'humd_value': instance.humd_value,
            'id': instance.id,
            'recorded_time': str(instance.recorded_time)
            })

@receiver(post_save, sender=LuxSensor)
def send_lux(sender, instance, created, **kwargs):
    if created:
        send_event('data_monitoring', 'lux_update', {
            'lux_value': instance.lux_value,
            'id': instance.id,
            'recorded_time': str(instance.recorded_time)
            })
  