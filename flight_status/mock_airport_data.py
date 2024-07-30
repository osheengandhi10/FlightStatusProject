import os
import django


# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_status.settings')
django.setup()

import random
import time
from flights.models import Flight
from flights.tasks import update_flight_status

def mock_airport_data():
    print("enter")
    flights = Flight.objects.all()
    statuses = ['On Time', 'Delayed', 'Cancelled']
    gates = ['A1', 'B2', 'C3', 'D4']

    while True:
        for flight in flights:
            status = random.choice(statuses)
            gate = random.choice(gates)
            print(flight.flight_number,flight.id, status, gate)
            update_flight_status.delay(flight.id, status, gate)
            time.sleep(5)  # Wait for 5 seconds before the next update

if __name__ == '__main__':
    mock_airport_data()