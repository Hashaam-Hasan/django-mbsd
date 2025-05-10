
from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Temp: {self.temperature} | Humi: {self.humidity} at {self.timestamp}"
# Create a table to store sensor data:



