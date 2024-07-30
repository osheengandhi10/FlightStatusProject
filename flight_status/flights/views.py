from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Flight
from .tasks import update_flight_status
from .serializers import FlightSerializer
from rest_framework import generics

""""
def get_flight_status(request):
    flight = Flight.objects.all()
    temp = FlightSerializer(flight)
    return Response(temp.data)
"""
class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

def update_flight(request, flight_number):
    status = request.POST.get('status')
    gate = request.POST.get('gate')
    if not status and not gate:
        status = 'Delayed'
        gate = 'A1'
    flight = Flight.objects.get(flight_number=flight_number)
    update_flight_status(flight.id, status, gate)
    print("updated status",flight.id, status, gate)
    return JsonResponse({'message': 'Flight status update initiated'})
