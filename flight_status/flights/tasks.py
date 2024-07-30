from celery import shared_task
from .models import Flight, Notification
from django.core.mail import send_mail
from twilio.rest import Client
import smtplib


@shared_task
def update_flight_status(flight_id, status, gate):
    flight = Flight.objects.get(id=flight_id)
    print(flight)
    flight.status = status
    flight.gate = gate
    flight.save()

    # Notify all users about the status change
    send_notifications(flight_id)

@shared_task
def send_notifications(flight_id):
    flight = Flight.objects.get(id=flight_id)
    print("notification ", flight)
    notifications = Notification.objects.filter(flight=flight)

    for notification in notifications:
        send_sms(notification.recipient, notification.message)
        

def send_sms(recipient, message):
    client = Client("AC4bc643098d9bfe4f03dae07a6ab69a5c", "2f1a879e5a4a47d39d076e7a7f25fcbc")
    client.messages.create(to=recipient, from_="+17627603977", body=message)

