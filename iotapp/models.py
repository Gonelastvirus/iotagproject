from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    token=models.CharField(max_length=17)
class Vegetable(models.Model):
    tarkari = models.CharField(max_length=100)
    temperature = models.CharField(max_length=10)
class SensorData(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    sensor_value= models.FloatField()
    timestamp = models.DateTimeField()

class DailySensorData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    average_sensor_value = models.FloatField()
