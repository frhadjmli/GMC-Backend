from django.db import models


# class Point(models.Model):
#     point_id = models.CharField(max_length=5) # e.g : PNT-1
#
#     def __str__(self):
#         return self.point_id
#
# class TempSensor(models.Model):
#     sensor_id = models.CharField(max_length=5) # e.g : TMP-1
#     temp_value = models.IntegerField()
#     recorded_time = models.TimeField(auto_now_add=True)
#     date_time = models.DateField(auto_now_add=True)
#     point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return f"{self.sensor_id}, record {self.pk}"
#
# class HumdSensor(models.Model):
#     sensor_id = models.CharField(max_length=5) # e.g : HUM-1
#     humd_value = models.IntegerField()
#     recorded_time = models.TimeField(auto_now_add=True)
#     date_time = models.DateField(auto_now_add=True)
#     point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return f"{self.sensor_id}, record {self.pk}"
#
# class LuxSensor(models.Model):
#     sensor_id = models.CharField(max_length=5) # e.g : LUX-1
#     lux_value = models.IntegerField()
#     recorded_time = models.TimeField(auto_now_add=True)
#     date_time = models.DateField(auto_now_add=True)
#     point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return f"{self.sensor_id}, record {self.pk}"
#
# class Ventilation(models.Model):
#     fan_id = models.CharField(max_length=5) # e.g : FAN-1
#     fan_status = models.BooleanField()
#     point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return f"{self.fan_id}, record {self.pk}"
#
# class Irrigation(models.Model):
#     pump_id = models.CharField(max_length=6) # e.g : WPMP-1
#     pump_status = models.BooleanField()
#     point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return f"{self.pump_id}, record {self.pk}"

class Sensor_type(models.Model):
    title = models.CharField(max_length=30)  # e.g : humidity, lux, temprature
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title}, record: {self.pk}"


class Point(models.Model):
    point_id = models.CharField(max_length=7)  # e.g : PNT-1

    def __str__(self):
        return f"{self.point_id}, record: {self.pk}"


class Sensor(models.Model):
    sensor_id = models.CharField(max_length=7)  # e.g : HUM-1, LUX-1, TMP-1    need this?
    name = models.CharField(max_length=50)  # e.g : DHT11, BH1750
    sensor_type = models.ForeignKey(Sensor_type, on_delete=models.DO_NOTHING)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}, record: {self.pk}"


class Sensor_value(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='sensor_values', on_delete=models.DO_NOTHING)
    value = models.FloatField()  # models.DecimalField( max_digits=7, decimal_places=2)  ,   models.IntegerField()
    recorded_time = models.TimeField()
    date_time = models.DateField()

    def __str__(self):
        return f"value: {self.value}, record: {self.pk} (sensor_id: {self.sensor})"


class Alarm_message(models.Model):
    body_text = models.CharField(max_length=255)
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    recorded_time = models.TimeField()
    date_time = models.DateField()

    def __str__(self):
        return f"{self.body_text[20]}, record: {self.pk}"


class Device_type(models.Model):
    title = models.CharField(max_length=30)  # e.g : fan, pump
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title}, record: {self.pk}"


class Device(models.Model):
    device_id = models.CharField(max_length=7)  # e.g : FAN-1, WPMP-1     need this?
    name = models.CharField(max_length=50)
    device_type = models.ForeignKey(Device_type, on_delete=models.DO_NOTHING)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}, record: {self.pk}"


class Device_value(models.Model):
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    status = models.BooleanField()
    recorded_time = models.TimeField()
    date_time = models.DateField()

    def __str__(self):
        return f"status: {self.status}, record: {self.pk} ( device_id: {self.device} )"
