from rest_framework import serializers
from .models import TempSensor, HumdSensor, LuxSensor, Ventilation, Irrigation


class TempSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempSensor
        fields = '__all__'


class HumdSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumdSensor
        fields = '__all__'


class LuxSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuxSensor
        fields = '__all__'


class VentilationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventilation
        fields = '__all__'


class IrrigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Irrigation
        fields = '__all__'
