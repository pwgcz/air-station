from rest_framework.views import APIView
from rest_framework.response import Response
from station_web.dust_sensor import measure


class SensorMeasurement(APIView):

    def get(self, request, format=None):
        measurement = measure()
        serialized_measurement = {'measurement': measurement, 'gegLan': None, 'gegLon':None}
        return Response(serialized_measurement)
