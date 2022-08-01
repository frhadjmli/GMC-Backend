from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import (TempSensorSerializer, HumdSensorSerializer, LuxSensorSerializer,
 VentilationSerializer, IrrigationSerializer)
from .models import TempSensor, HumdSensor, LuxSensor, Ventilation, Irrigation


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

class HumdSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = HumdSensor.objects.all()
        serializer = HumdSensorSerializer(qs, many=True)
        return Response(serializer.data)


class LuxSensorView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = LuxSensor.objects.all()
        serializer = LuxSensorSerializer(qs, many=True)
        return Response(serializer.data)


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


