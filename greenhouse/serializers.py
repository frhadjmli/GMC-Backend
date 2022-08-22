from rest_framework import serializers

from .models import SensorTypeRange


class SensorTypeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorTypeRange
        exclude = ['sensor_type']

    def validate(self, data):
        if data.get('min_range', 0) > data.get('max_range', 0):
            error = 'Maximum range should be greater than minimum range'
            raise serializers.ValidationError(error)

        return data

    def validate_min_range(self, value):
        if value < 0:
            raise serializers.ValidationError('Minimum range must be postive')

        return value

    def validate_max_range(self, value):
        if value < 0:
            raise serializers.ValidationError('Maximum range must be postive')

        return value
