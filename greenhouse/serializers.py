from rest_framework import serializers
from .models import Sensor, SensorValue

class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorValue
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    sensor_values = SensorValueSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'sensor_type', 'point', 'sensor_values']
        depth = 2



