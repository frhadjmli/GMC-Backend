from rest_framework import serializers

from .models import SensorTypeRange


class SensorTypeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorTypeRange
        exclude = ['sensor_type']
