from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import F
from .models import Sensor, SensorType, SensorValue, DeviceValue
from .serializers import SensorSerializer, SensorValueSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint' : "/login/",
            'method' : "POST",
        }
    ]
    return Response(routes)


class SensorView(APIView):
    def get(self, request, *arg, **kwargs):
        # qs = Sensors.objects.all()
        qs = Sensor.objects.filter(sensor_type=1)
        serializer = SensorSerializer(qs, many=True)
        return Response(serializer.data)


class SensorValueView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = SensorValue.objects.all()
        serializer = SensorValueSerializer(qs, many=True)
        return Response(serializer.data)


class TempSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        
        qs = SensorValue.objects.select_related('sensor').select_related('point_id').select_related('sensor_type_id') \
            .filter(sensor_id__sensor_type_id=1) \
            .annotate(sensor_Id=F('sensor_id__sensor_id'), sensor_type=F('sensor_id__sensor_type__title'),
                      sensor_name=F('sensor_id__name'), point_id=F('sensor_id__point_id__point_id'), ) \
            .values('id', 'value', 'recorded_time', 'date_time', 'sensor_Id', 'sensor_type', 'sensor_name', 'point_id')

        return Response(list(qs))

    def post(self, request):
        # sensor_id -> TMP-1 : 1 , HUM-1 : 2 , LUX-1: 3   check value in database (table: greenhouse_sensor)
        temperature = SensorValue.objects.create(
            sensor=get_object_or_404(Sensor, id=request.data.get('sensor_id')),
            value=request.data.get('temp_value'),
            # recorded_time=request.data.get('current_time'),  # define auto_now_add
            # date_time=request.data.get('current_date'),  # define auto_now_add
        )
        return Response({
            'Message': f"New Temperature({temperature.value}) Registered"},
            status=status.HTTP_201_CREATED
        )


class HumidSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = SensorValue.objects.select_related('sensor').select_related('point_id').select_related('sensor_type_id') \
            .filter(sensor_id__sensor_type_id=2) \
            .annotate(sensor_Id=F('sensor_id__sensor_id'), sensor_type=F('sensor_id__sensor_type__title'),
                      sensor_name=F('sensor_id__name'), point_id=F('sensor_id__point_id__point_id'), ) \
            .values('id', 'value', 'recorded_time', 'date_time', 'sensor_Id', 'sensor_type', 'sensor_name', 'point_id')

        return Response(list(qs))

    # def post(self, request):
    #     humidity = HumdSensor.objects.create(
    #         sensor_id = request.data.get('sensor_id'),
    #         humd_value = request.data.get('humd_value'),
    #         recorded_time = request.data.get('current_time'),
    #         date_time = request.data.get('current_date'),
    #         point = Point.objects.get(id=request.data.get('point_id')),
    #     )
    #     return Response({
    #         'Message':f"New Humidity({humidity.humd_value}) Registered"},
    #         status=status.HTTP_201_CREATED
    #     )


class LuxSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = SensorValue.objects.select_related('sensor').select_related('point_id').select_related('sensor_type_id') \
            .filter(sensor_id__sensor_type_id=3) \
            .annotate(sensor_Id=F('sensor_id__sensor_id'), sensor_type=F('sensor_id__sensor_type__title'),
                      sensor_name=F('sensor_id__name'), point_id=F('sensor_id__point_id__point_id'), ) \
            .values('id', 'value', 'recorded_time', 'date_time', 'sensor_Id', 'sensor_type', 'sensor_name', 'point_id')

        return Response(list(qs))

    # def post(self, request):
    #     lux = LuxSensor.objects.create(
    #         sensor_id = request.data.get('sensor_id'),
    #         lux_value = request.data.get('lux_value'),
    #         recorded_time = request.data.get('current_time'),
    #         date_time = request.data.get('current_date'),
    #         point = Point.objects.get(id=request.data.get('point_id')),
    #     )
    #     return Response({
    #         'Message':f"New Lux({lux.lux_value}) Registered"},
    #         status=status.HTTP_201_CREATED
    #         )


class VentilationView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = DeviceValue.objects.select_related('device').select_related('point_id').select_related('device_type_id') \
            .filter(device_id__device_type_id=1) \
            .annotate(device_Id=F('device_id__device_id'), device_type=F('device_id__device_type__title'),
                      device_name=F('device_id__name'), point_id=F('device_id__point_id__point_id'), ) \
            .values('id', 'status', 'recorded_time', 'date_time', 'device_Id', 'device_type', 'device_name', 'point_id')

        return Response(list(qs))

    def put(self, request, device_id):
        ventilation = get_object_or_404(DeviceValue, device=device_id)

        ventilation.status = False if ventilation.status == True else True
        ventilation.save()
        return Response({'message': 'updated successfully!', 'fan_status': ventilation.status})


class IrrigationView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = DeviceValue.objects.select_related('device').select_related('point_id').select_related('device_type_id') \
            .filter(device_id__device_type_id=2) \
            .annotate(device_Id=F('device_id__device_id'), device_type=F('device_id__device_type__title'),
                      device_name=F('device_id__name'), point_id=F('device_id__point_id__point_id'), ) \
            .values('id', 'status', 'recorded_time', 'date_time', 'device_Id', 'device_type', 'device_name', 'point_id')

        return Response(list(qs))

    def put(self, request, device_id):
        irrigation = get_object_or_404(DeviceValue, device=device_id)

        irrigation.status = False if irrigation.status == True else True
        irrigation.save()
        return Response({'message': 'updated successfully!', 'pump_status': irrigation.status})
