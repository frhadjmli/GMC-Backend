from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import F
from django.db.models.functions import Replace
# from .serializers import (TempSensorSerializer, HumdSensorSerializer, LuxSensorSerializer,
#  VentilationSerializer, IrrigationSerializer)
# from .models import Point, TempSensor, HumdSensor, LuxSensor, Ventilation, Irrigation
from .models import Sensor, Sensor_type, Sensor_value, Device_value
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
#
#
# class TempSensorView(APIView):
#     def get(self, request, *arg, **kwargs):
#         qs = TempSensor.objects.all()
#         serializer = TempSensorSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         temperature = TempSensor.objects.create(
#             sensor_id = request.data.get('sensor_id'),
#             temp_value = request.data.get('temp_value'),
#             recorded_time = request.data.get('current_time'),
#             date_time = request.data.get('current_date'),
#             point = Point.objects.get(id=request.data.get('point_id')),
#         )
#         return Response({
#             'Message':f"New Temperature({temperature.temp_value}) Registered"},
#             status=status.HTTP_201_CREATED
#         )
#
# class HumdSensorView(APIView):
#     def get(self, request, *arg, **kwargs):
#         qs = HumdSensor.objects.all()
#         serializer = HumdSensorSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         humidity = HumdSensor.objects.create(
#             sensor_id = request.data.get('sensor_id'),
#             humd_value = request.data.get('humd_value'),
#             recorded_time = request.data.get('current_time'),
#             date_time = request.data.get('current_date'),
#             point = Point.objects.get(id=request.data.get('point_id')),
#         )
#         return Response({
#             'Message':f"New Humidity({humidity.humd_value}) Registered"},
#             status=status.HTTP_201_CREATED
#         )
#
# class LuxSensorView(APIView):
#     def get(self, request, *arg, **kwargs):
#         qs = LuxSensor.objects.all()
#         serializer = LuxSensorSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         lux = LuxSensor.objects.create(
#             sensor_id = request.data.get('sensor_id'),
#             lux_value = request.data.get('lux_value'),
#             recorded_time = request.data.get('current_time'),
#             date_time = request.data.get('current_date'),
#             point = Point.objects.get(id=request.data.get('point_id')),
#         )
#         return Response({
#             'Message':f"New Lux({lux.lux_value}) Registered"},
#             status=status.HTTP_201_CREATED
#             )
#
# class VentilationView(APIView):
#     def get(self, request, *arg, **kwargs):
#         qs = Ventilation.objects.all()
#         serializer = VentilationSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def put(self, request, ventilation_id):
#         ventilation = get_object_or_404(Ventilation, id=ventilation_id)
#
#         ventilation.fan_status = False if ventilation.fan_status == True else True
#         ventilation.save()
#         return Response({'message': 'updated successfully!', 'fan_status': ventilation.fan_status})
#
#
# class IrrigationView(APIView):
#     def get(self, request, *arg, **kwargs):
#         qs = Irrigation.objects.all()
#         serializer = IrrigationSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def put(self, request, irrigation_id):
#         irrigation = get_object_or_404(Irrigation, id=irrigation_id)
#
#         irrigation.pump_status = False if irrigation.pump_status == True else True
#         irrigation.save()
#         return Response({'message': 'updated successfully!', 'pump_status': irrigation.pump_status})


class SensorView(APIView):
    def get(self, request, *arg, **kwargs):
        # qs = Sensors.objects.all()
        qs = Sensor.objects.filter(sensor_type=1)
        serializer = SensorSerializer(qs, many=True)
        return Response(serializer.data)


class SensorValueView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = Sensor_value.objects.all()
        serializer = SensorValueSerializer(qs, many=True)
        return Response(serializer.data)


class TempSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = Sensor_value.objects.select_related('sensor').select_related('point_id').select_related('sensor_type_id') \
            .filter(sensor_id__sensor_type_id=1) \
            .annotate(sensor_Id=F('sensor_id__sensor_id'), sensor_type=F('sensor_id__sensor_type__title'),
                      sensor_name=F('sensor_id__name'), point_id=F('sensor_id__point_id__point_id'), ) \
            .values('id', 'value', 'recorded_time', 'date_time', 'sensor_Id', 'sensor_type', 'sensor_name', 'point_id')

        return Response(list(qs))

    # def post(self, request):
    #     temperature = TempSensor.objects.create(
    #         sensor_id = request.data.get('sensor_id'),
    #         temp_value = request.data.get('temp_value'),
    #         recorded_time = request.data.get('current_time'),
    #         date_time = request.data.get('current_date'),
    #         point = Point.objects.get(id=request.data.get('point_id')),
    #     )
    #     return Response({
    #         'Message':f"New Temperature({temperature.temp_value}) Registered"},
    #         status=status.HTTP_201_CREATED
    #     )


class HumidSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = Sensor_value.objects.select_related('sensor').select_related('point_id').select_related('sensor_type_id') \
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
        qs = Sensor_value.objects.select_related('sensor').select_related('point_id').select_related('sensor_type_id') \
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
        qs = Device_value.objects.select_related('device').select_related('point_id').select_related('device_type_id') \
            .filter(device_id__device_type_id=1) \
            .annotate(device_Id=F('device_id__device_id'), device_type=F('device_id__device_type__title'),
                      device_name=F('device_id__name'), point_id=F('device_id__point_id__point_id'), ) \
            .values('id', 'status', 'recorded_time', 'date_time', 'device_Id', 'device_type', 'device_name', 'point_id')

        return Response(list(qs))

    # def put(self, request, ventilation_id):
    #     ventilation = get_object_or_404(Ventilation, id=ventilation_id)
    #
    #     ventilation.fan_status = False if ventilation.fan_status == True else True
    #     ventilation.save()
    #     return Response({'message': 'updated successfully!', 'fan_status': ventilation.fan_status})


class IrrigationView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = Device_value.objects.select_related('device').select_related('point_id').select_related('device_type_id') \
            .filter(device_id__device_type_id=2) \
            .annotate(device_Id=F('device_id__device_id'), device_type=F('device_id__device_type__title'),
                      device_name=F('device_id__name'), point_id=F('device_id__point_id__point_id'), ) \
            .values('id', 'status', 'recorded_time', 'date_time', 'device_Id', 'device_type', 'device_name', 'point_id')

        return Response(list(qs))

    # def put(self, request, irrigation_id):
    #     irrigation = get_object_or_404(Irrigation, id=irrigation_id)
    #
    #     irrigation.pump_status = False if irrigation.pump_status == True else True
    #     irrigation.save()
    #     return Response({'message': 'updated successfully!', 'pump_status': irrigation.pump_status})
