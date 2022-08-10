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


class City(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}, record {self.pk}"


class Greenhouse(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=200)
    allay = models.CharField(max_length=50)
    post_code = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.name}, record {self.pk}"


class Sensor_type(models.Model):
    title = models.CharField(max_length=30)  # e.g : humidity, lux, temprature
    model_name = models.CharField(max_length=50)  # e.g : dh11
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}, record {self.pk}"


class Point(models.Model):
    point_name = models.CharField(max_length=7)  # e.g : PNT-1

    def __str__(self):
        return f"{self.point_name}, record {self.pk}"


class Sensors(models.Model):
    name = models.CharField(max_length=50)  # e.g : HUM-1, LUX-1, TMP-1    need this?
    sensor_type = models.ForeignKey(Sensor_type, on_delete=models.DO_NOTHING)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}, record {self.pk}"


class Sensor_value(models.Model):
    sensor_id = models.ForeignKey(Sensors, on_delete=models.DO_NOTHING)
    value = models.FloatField()  # models.DecimalField( max_digits=7, decimal_places=2)  ,   models.IntegerField()
    recorded_time = models.TimeField(auto_now_add=True)
    date_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, record {self.pk}"


class Device_type(models.Model):
    title = models.CharField(max_length=30)  # e.g : fan, pump
    model_name = models.CharField(max_length=50)  # e.g : dh11
    description = models.CharField(max_length=255)


class Devices(models.Model):
    name = models.CharField(max_length=50)  # e.g : FAN-1, WPMP-1     need this?
    device_type = models.ForeignKey(Device_type, on_delete=models.DO_NOTHING)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.DO_NOTHING)


class Device_status(models.Model):
    devices_id = models.ForeignKey(Devices, on_delete=models.DO_NOTHING)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.name}, record {self.pk}"