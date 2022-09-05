from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import SensorTypeRangeSerializer
from django.db.models import F
from .models import Sensor, AlarmMessage, SensorValue, DeviceValue, Device, SensorTypeRange
from persiantools.jdatetime import JalaliDate
from datetime import datetime
from rest_framework.permissions import IsAdminUser

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
        item.date_time = str(JalaliDate.today())
        item.recorded_time = (datetime.now()).strftime('%H:%M:%S')
        item.save()
        return Response({'message': 'updated successfully!',
                         'status': item.status,
                         'device_id': item.device_id,
                         'date_time': item.date_time,
                         'recorded_time': item.recorded_time
                         })


class AlarmMessageView(APIView):
    def get(self, request):
        qs = AlarmMessage.objects.select_related('sensorValue'). \
            annotate(sensor_id=F('sensorValue_id__sensor_id'),
                     value=F('sensorValue_id__value'),
                     recorded_time=F('sensorValue_id__recorded_time'),
                     date_time=F('sensorValue_id__date_time')).values()

        return Response(list(qs))

    def put(self, request):
        AlarmMessage.objects.filter(is_seen=False).update(is_seen=True)
        return Response({'message': 'updated successfully!'})


class AlarmMessageIsSeenView(APIView):
    def get(self, request):
        qs = AlarmMessage.objects.select_related('sensorValue').filter(is_seen=False) \
            .annotate(value=F('sensorValue_id__value'),
                      recorded_time=F('sensorValue_id__recorded_time'),
                      date_time=F('sensorValue_id__date_time')).values()

        return Response(list(qs))


class CountSensorDeviceView(APIView):
    def get(self, request):
        device_count = Device.objects.all().count()
        sensor_count = Sensor.objects.all().count()

        return Response({'device_count': device_count, 'sensor_count': sensor_count})


class SensorTypeRangeView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        qs = SensorTypeRange.objects.select_related('sensor_type').annotate(title=F('sensor_type__title')).values()

        return Response(list(qs))

    def put(self, request, sensor_type_range_id):
        sensor_type_range = get_object_or_404(SensorTypeRange, id=sensor_type_range_id)
        serializer = SensorTypeRangeSerializer(
            instance=sensor_type_range,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'updated successfully!', 'data': serializer.data})

        return Response({'message': serializer.errors})
