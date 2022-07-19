from django.db import models


class Point(models.Model):
    point_id = models.CharField(max_length=5) # e.g : PNT-1

    def __str__(self):
        return self.point_id 

class TempSensor(models.Model):
    sensor_id = models.CharField(max_length=5) # e.g : TMP-1
    temp_value = models.IntegerField()
    recorded_time = models.TimeField(auto_now_add=True)
    date_time = models.DateField(auto_now_add=True)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.sensor_id}, record {self.pk}"

class HumdSensor(models.Model):
    sensor_id = models.CharField(max_length=5) # e.g : HUM-1
    humd_value = models.IntegerField()
    recorded_time = models.TimeField(auto_now_add=True)
    date_time = models.DateField(auto_now_add=True)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.sensor_id}, record {self.pk}"

class LuxSensor(models.Model):
    sensor_id = models.CharField(max_length=5) # e.g : LUX-1
    lux_value = models.IntegerField()
    recorded_time = models.TimeField(auto_now_add=True)
    date_time = models.DateField(auto_now_add=True)
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.sensor_id}, record {self.pk}"

class Ventilation(models.Model):
    fan_id = models.CharField(max_length=5) # e.g : FAN-1
    fan_status = models.BooleanField()
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.fan_id}, record {self.pk}"

class Irrigation(models.Model):
    pump_id = models.CharField(max_length=6) # e.g : WPMP-1
    pump_status = models.BooleanField()
    point = models.ForeignKey(Point, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.pump_id}, record {self.pk}"


    
    
