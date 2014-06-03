from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime
# Create your models here.

class Person(models.Model):
	user = models.ForeignKey(User)
	households = models.CharField(max_length=10)
	acreage = models.CharField(max_length=20)
	completed_date = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.name
	def __unicode__(self):
		return '%s' % (self.email)

class Location(models.Model):
	climate = models.CharField(max_length=200)
	season = models.CharField(max_length=200)
	moisture = models.CharField(max_length=200)
	direction = models.CharField(max_length=200)
	other = models.CharField(max_length=2000)

	def __unicode__(self):
		return self.other

# Need a Sensor Type and Devices & Devices Types model        
class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True, unique=True, db_index=True)
    head_unit_id = models.IntegerField()
    closest_valve = models.IntegerField()
    sensor_type = models.IntegerField()
    time_data_collected = models.TextField()
    amount_rained = models.DecimalField(max_digits=5, decimal_places=2)
    length_of_increased_moisture = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.sensor_id)
    
class Zone(models.Model):
    zone_name = models.CharField(max_length=200)
    def __str__(self):
        return self.zone_name
        

class Plant(models.Model):
    plant_name = models.CharField(max_length=200)
    plant_type = models.CharField(max_length=200)
    plant_soil_type = models.CharField(max_length=200)
    location = models.IntegerField()
    def __str__(self):
        return self.plant_name
		
#Used for Plant db and table
class LocationChoice(models.Model):
    plant = models.ForeignKey(Plant)
    location_choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.location_choice_text

class DeviceType(models.Model):
    device_name = models.CharField(max_length=200)
    device_display_name = models.CharField(max_length=200)
    def __str__(self):
        return self.device_name

class Device(models.Model):
    zone = models.ForeignKey(Zone)
    device_type = models.ForeignKey(DeviceType)
    device_serial_number = models.CharField(max_length=200)
    zones_affected = models.CharField(max_length=200)
    device_display_name = models.CharField(max_length=200)
    device_location = models.IntegerField()
    registered = models.BooleanField()
    #head unit id
    #customer id
    def __str__(self):
        return self.device_name
