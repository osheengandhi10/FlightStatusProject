from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    gate = models.CharField(max_length=10)

    def __str__(self):
        return self.flight_number

class Notification(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=100)
    channel = models.CharField(max_length=10, choices=[('SMS', 'SMS')])
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.flight.flight_number} to {self.recipient}"
