import logging

from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Event, Sensor
from api.serializers import EventSerializer, SensorSerializer

logger = logging.getLogger(__name__)

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
        key = self.request.query_params.get('key')
        if sensor_id:
            logger.warn('Received sensor_id')
            queryset = queryset.filter(sensor_id=sensor_id)
        if key:
            queryset = queryset.filter(key=key)
        return queryset


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    @action(detail=True, methods=['post'], url_path='')
    def event(self, request, pk):
        """ Function to create the sensor if not existing and save the event in the database. """
        response = {}

        # Let's try to retrive the sensor or create.
        try:
            sensor = Sensor.objects.get(external_id=pk)
        
        except Sensor.DoesNotExist as e:
            logger.info(
                f"{e} - Error getting Sensor, we will create sensor. ")

            # If we don't have a sensor, we create
            sensor = Sensor.objects\
                .create(
                    external_id=pk
                )

            # Now create the event

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
