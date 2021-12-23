from django.db.models import query
from django.shortcuts import render
from rest_framework import filters, permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Event, Sensor
from api.serializers import EventSerializer, SensorSerializer

# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
          """ Filter by some fields. """
          queryset = Event.objects.all()
          sensor_id = self.request.query_params.get('sensor_id')
          if sensor_id:
              queryset = queryset.filter(sensor_id=sensor_id)
          return queryset        



class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    @action(detail=True, methods=['post'], url_path='')
    def event(self, request, pk=None):
        response = {}
        if pk is None:
            response["message"] = "Required pk."
            return Response(response, status.HTTP_400_BAD_REQUEST)
        else:
            try:
                 # Let's retrive the sensor.
                sensor = Sensor.objects.get(external_id=pk)
            except:
                # If we don't have a sensor, we create
                sensor = Sensor.objects.create(
                    external_id=pk
                )

            if 'key' in request.data and 'value' in request.data and 'unit' in request.data:
                event = Event.objects.create(
                    key=request.data['key'],
                    unit=request.data['unit'],
                    value=request.data['value'],
                    sensor=sensor
                )
                response['message'] = "Created event"
                serializer = EventSerializer(event, many=False)
                response['data'] = serializer.data
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                response["message"] = "Required key, value, unit."
                return Response(response, status.HTTP_400_BAD_REQUEST)