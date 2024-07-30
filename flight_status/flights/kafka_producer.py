import json
from kafka import KafkaProducer
from django.conf import settings
import firebase_admin
from firebase_admin import messaging

producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_flight_update(flight_data):
    producer.send(settings.KAFKA_TOPIC, flight_data)
    send_notification(flight_data)

def send_notification(flight_data):
    message = messaging.Message(
        data=flight_data,
        topic="flight_updates",
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)
