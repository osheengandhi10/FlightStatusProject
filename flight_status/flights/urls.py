from django.urls import path
from .views import FlightListView, update_flight

urlpatterns = [
    #path('status/', get_flight_status, name='get_flight_status'),
    path('status/', FlightListView.as_view(), name='flight-list'),
    path('update/<str:flight_number>/', update_flight, name='update_flight'),
]
