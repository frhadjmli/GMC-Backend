from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import TempSensorSerializer, HumdSensorSerializer, LuxSensorSerializer, VentilationSerializer, IrrigationSerializer
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

    # def post(self, request, *arg, **kwargs):
    #     serializer = TempSensorSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message': 'info added successfully!', 'data': serializer.data})
    #
    #     return Response({'message': serializer.errors})


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


class IrrigationView(APIView):
    def get(self, request, *arg, **kwargs):
        qs = Irrigation.objects.all()
        serializer = IrrigationSerializer(qs, many=True)
        return Response(serializer.data)
