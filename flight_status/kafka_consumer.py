# Set up Django environment
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_status.settings')
django.setup()

import json
from kafka import KafkaConsumer
from django.conf import settings
from flights.models import Flight
from kafka import KafkaConsumer
import json



def consume():
    print("enter consume")
    consumer = KafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_SERVER,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    print("consumer is ", consumer)

    for message in consumer:
        flight_data = message.value
        flight = Flight.objects.get(flight_number=flight_data['flight_number'])
        flight.status = flight_data['status']
        flight.gate = flight_data['gate']
        flight.save()
        print(f'Updated flight: {flight.flight_number}')


if __name__ == "__main__":
    consume()
