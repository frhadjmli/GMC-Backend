from django.db.models import F
from .models import SensorValue, AlarmMessage, SensorTypeRange
from django.http import Http404


def retrive_renge_val():
    range_value = {
        # 'Temperature': [],
        # 'Humidity': [],
        # 'Lux': []
    }
    qs = SensorTypeRange.objects.select_related('sensortype').annotate(title=F('sensor_type_id__title')).values()
    for item in list(qs):
        range_value[item['title']] = []
        range_value[item['title']].append(item['min_range'])
        range_value[item['title']].append(item['max_range'])
    return range_value


def detect_alarm(range_val, instance, message=""):

    if float(instance.value) < range_val[0]:
        message = message + "کم تر از حد مجاز"
        AlarmMessage.objects.create(body_text=message, sensorValue=SensorValue.objects.get(id=instance.id))

    elif float(instance.value) > range_val[1]:
        message = message + "بیشتر تر از حد مجاز"
        AlarmMessage.objects.create(body_text=message, sensorValue=SensorValue.objects.get(id=instance.id))
    return


def get_extra_data_from_alarm_message(alarm_message_id):

    qs = AlarmMessage.objects.select_related('sensorValue').select_related('sensor').filter(id=alarm_message_id). \
        annotate(sensor_id=F('sensorValue_id__sensor_id__sensor_id'),
                 recorded_time=F('sensorValue_id__recorded_time'),
                 date_time=F('sensorValue_id__date_time')).values()
    qs = list(qs)
    if len(qs) == 0:
        raise Http404(
            "No matches the given query."
        )

    return qs[0]
