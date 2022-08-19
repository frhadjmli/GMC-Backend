from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.db.models import F
from .models import Sensor, AlarmMessage, SensorValue, DeviceValue


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint' : "/login/",
            'method' : "POST",
        }
    ]
    return Response(routes)


class SensorValueInfoView(APIView):
    def get(self, request, sensor_type_id):
        
        qs = SensorValue.objects.select_related('sensor').select_related('point_id').select_related('sensor_type_id') \
            .filter(sensor_id__sensor_type_id=sensor_type_id) \
            .annotate(sensor_Id=F('sensor_id__sensor_id'), sensor_type=F('sensor_id__sensor_type__title'),
                      sensor_name=F('sensor_id__name'), point_id=F('sensor_id__point_id__point_id'), ) \
            .values('id', 'value', 'recorded_time', 'date_time', 'sensor_Id', 'sensor_type', 'sensor_name', 'point_id')

        return Response(list(qs))

    def post(self, request):
        # sensor_id -> TMP-1 : 1 , HUM-1 : 2 , LUX-1: 3 
        item = SensorValue.objects.create(
            sensor=get_object_or_404(Sensor, id=request.data.get('sensor_id')),
            value=request.data.get('value'),
            recorded_time=request.data.get('current_time'), 
            date_time=request.data.get('current_date'),  
        )
        return Response({
            'Message': f"New item value ({item.value}) Registered with sensor_id: {item.sensor_id}"},
            status=status.HTTP_201_CREATED
        )


class DeviceValueInfoView(APIView):
    def get(self, request, device_type_id):
        qs = DeviceValue.objects.select_related('device').select_related('point_id').select_related('device_type_id') \
            .filter(device_id__device_type_id=device_type_id) \
            .annotate(device_Id=F('device_id__device_id'), device_type=F('device_id__device_type__title'),
                      device_name=F('device_id__name'), point_id=F('device_id__point_id__point_id'), ) \
            .values('id', 'status', 'recorded_time', 'date_time', 'device_Id', 'device_type', 'device_name', 'point_id')

        return Response(list(qs))

    def put(self, request, device_id):
        # device_id -> FAN-1 : 1 , WPMP-1 : 2
        item = get_object_or_404(DeviceValue, device=device_id)

        item.status = False if item.status == True else True
        item.save()
        return Response({'message': 'updated successfully!', 'status': item.status, 'device_id': item.device_id})


class AlarmMessageView(APIView):
    def get(self, request):
        qs = AlarmMessage.objects.all().values()

        return Response(list(qs))

    def put(self, request):
        AlarmMessage.objects.filter(is_seen=False).update(is_seen=True)
        return Response({'message': 'updated successfully!'})


class AlarmMessageIsSeenView(APIView):
    def get(self, request):
        qs = AlarmMessage.objects.filter(is_seen=False).values()

        return Response(list(qs))
