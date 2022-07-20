from rest_framework import serializers
from .models import TempSensor


class TempSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempSensor
        fields = '__all__'
