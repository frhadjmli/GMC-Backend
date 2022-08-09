from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import (TempSensorSerializer, HumdSensorSerializer, LuxSensorSerializer,
 VentilationSerializer, IrrigationSerializer)
from .models import Point, TempSensor, HumdSensor, LuxSensor, Ventilation, Irrigation


# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint' : "/login/",
            'method' : "POST",
        }
    ]
    return Response(routes)


class TempSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = TempSensor.objects.all()
        serializer = TempSensorSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        temperature = TempSensor.objects.create(
            sensor_id = request.data.get('sensor_id'),
            temp_value = request.data.get('temp_value'),
            recorded_time = request.data.get('current_time'),
            date_time = request.data.get('current_date'),
            point = Point.objects.get(id=request.data.get('point_id')),
        )
        return Response({
            'Message':f"New Temperature({temperature.temp_value}) Registered"},
            status=status.HTTP_201_CREATED
        )

class HumdSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = HumdSensor.objects.all()
        serializer = HumdSensorSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        humidity = HumdSensor.objects.create(
            sensor_id = request.data.get('sensor_id'),
            humd_value = request.data.get('humd_value'),
            recorded_time = request.data.get('current_time'),
            date_time = request.data.get('current_date'),
            point = Point.objects.get(id=request.data.get('point_id')),
        )
        return Response({
            'Message':f"New Humidity({humidity.humd_value}) Registered"},
            status=status.HTTP_201_CREATED
        )

class LuxSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = LuxSensor.objects.all()
        serializer = LuxSensorSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        lux = LuxSensor.objects.create(
            sensor_id = request.data.get('sensor_id'),
            lux_value = request.data.get('lux_value'),
            recorded_time = request.data.get('current_time'),
            date_time = request.data.get('current_date'),
            point = Point.objects.get(id=request.data.get('point_id')),
        )
        return Response({
            'Message':f"New Lux({lux.lux_value}) Registered"},
            status=status.HTTP_201_CREATED
            )

class VentilationView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = Ventilation.objects.all()
        serializer = VentilationSerializer(qs, many=True)
        return Response(serializer.data)

    def put(self, request, ventilation_id):
        ventilation = get_object_or_404(Ventilation, id=ventilation_id)

        ventilation.fan_status = False if ventilation.fan_status == True else True
        ventilation.save()
        return Response({'message': 'updated successfully!', 'fan_status': ventilation.fan_status})


class IrrigationView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = Irrigation.objects.all()
        serializer = IrrigationSerializer(qs, many=True)
        return Response(serializer.data)

    def put(self, request, irrigation_id):
        irrigation = get_object_or_404(Irrigation, id=irrigation_id)

        irrigation.pump_status = False if irrigation.pump_status == True else True
        irrigation.save()
        return Response({'message': 'updated successfully!', 'pump_status': irrigation.pump_status})


