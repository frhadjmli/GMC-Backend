from rest_framework import serializers
# from .models import TempSensor, HumdSensor, LuxSensor, Ventilation, Irrigation
from .models import Sensor, Sensor_value

# class TempSensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TempSensor
#         fields = '__all__'
#
#
# class HumdSensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HumdSensor
#         fields = '__all__'
#
#
# class LuxSensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LuxSensor
#         fields = '__all__'
#
#
# class VentilationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ventilation
#         fields = '__all__'
#
#
# class IrrigationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Irrigation
#         fields = '__all__'


class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_value
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    sensor_values = SensorValueSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'sensor_type', 'point', 'sensor_values']
        depth = 2



