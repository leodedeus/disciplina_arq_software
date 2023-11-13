from django.db import models

# Create your models here.

class Stations(models.Model):
    id = models.AutoField(primary_key=True)
    station = models.CharField(max_length=200)
    station_number = models.IntegerField(null=True, blank=True)
    station_name = models.CharField(max_length=200)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    
class Rides(models.Model):
    id = models.AutoField(primary_key=True)
    user_gender = models.CharField(max_length=5)
    user_birthdate = models.DateField(null=True, blank=True)
    user_residence = models.CharField(max_length=200)
    ride_date = models.DateField(null=True, blank=True)
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    station_start = models.CharField(max_length=200)
    station_end = models.CharField(max_length=200)
    ride_duration = models.FloatField(null=True, blank=True)
    ride_late = models.IntegerField(null=True, blank=True)
    
    