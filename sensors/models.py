from django.db import models
from django.contrib.auth.models import User

class Sensor(models.Model):
    SENSOR_TYPE_CHOICES = [
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('wind', 'Wind'),
        ('rain', 'Rain'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=SENSOR_TYPE_CHOICES)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.type} sensor (model: {self.model})"

class Data(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    rain = models.FloatField(null=True, blank=True)

class Alert(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
