from django.db import models

class SensorType(models.Model):
    title = models.CharField(max_length=30)  # e.g : humidity, lux, temprature
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title}, record: {self.pk}"

class Point(models.Model):
    point_id = models.CharField(max_length=7)  # e.g : PNT-1

    def __str__(self):
        return f"{self.point_id}, record: {self.pk}"

class Sensor(models.Model):
    sensor_id = models.CharField(max_length=7)  # e.g : HUM-1, LUX-1, TMP-1 
    name = models.CharField(max_length=50)  # e.g : DHT11, BH1750
    sensor_type = models.ForeignKey(SensorType, on_delete=models.DO_NOTHING)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}, record: {self.pk}"

class SensorValue(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='sensor_values', on_delete=models.DO_NOTHING)
    value = models.FloatField()  # models.DecimalField( max_digits=7, decimal_places=2)  ,   models.IntegerField()
    recorded_time = models.TimeField()
    date_time = models.DateField()

    def __str__(self):
        return f"value: {self.value}, record: {self.pk} (sensor_id: {self.sensor})"

class AlarmMessage(models.Model):
    body_text = models.CharField(max_length=255)
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    recorded_time = models.TimeField()
    date_time = models.DateField()

    def __str__(self):
        return f"{self.body_text[:12]+' ...'}, record: {self.pk}"

class DeviceType(models.Model):
    title = models.CharField(max_length=30)  # e.g : fan, pump
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title}, record: {self.pk}"

class Device(models.Model):
    device_id = models.CharField(max_length=7)  # e.g : FAN-1, WPMP-1     need this?
    name = models.CharField(max_length=50)
    device_type = models.ForeignKey(DeviceType, on_delete=models.DO_NOTHING)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}, record: {self.pk}"

class DeviceValue(models.Model):
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    status = models.BooleanField()
    recorded_time = models.TimeField()
    date_time = models.DateField()

    def __str__(self):
        return f"status: {self.status}, record: {self.pk} ( device_id: {self.device} )"
