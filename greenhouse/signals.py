import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_eventstream import send_event

from .models import TempSensor, HumdSensor

# @receiver(post_save, sender=TempSensor)
# def send_temperature(sender, instance, created, **kwargs):
#     if created:
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)('temperatures', {
#             'type':'temperature_update',
#             'text': json.dumps({
#                 'temp_value': instance.temp_value,
#                 'recorded_time': str(instance.recorded_time)
#             })
#         })

@receiver(post_save, sender=TempSensor)
def send_temperature(sender, instance, created, **kwargs):
    if created:
        send_event('data_monitoring', 'temp_update', {
            'temp_value': instance.temp_value,
            'id': instance.id,
            # 'recorded_time': str(instance.recorded_time)
            })
  