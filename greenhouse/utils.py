from django.db.models import F
from .models import Sensor, AlarmMessage, SensorTypeRange


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
        AlarmMessage.objects.create(body_text=message, sensor=Sensor.objects.get(id=instance.sensor_id),
                                    recorded_time=instance.recorded_time, date_time=instance.date_time)

    elif float(instance.value) > range_val[1]:
        message = message + "بیشتر تر از حد مجاز"
        AlarmMessage.objects.create(body_text=message, sensor=Sensor.objects.get(id=instance.sensor_id),
                                    recorded_time=instance.recorded_time, date_time=instance.date_time)
    return
