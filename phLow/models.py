from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime
# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=200)
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

class Sensors(models.Model):
    
    sensorid = models.AutoField(primary_key=True, unique=True, db_index=True)
    headunitid = models.IntegerField()
    closest_valve = models.IntegerField()
    sensor_type = models.IntegerField()
    time_data_collected = models.TextField()
    amount_rained = models.DecimalField(max_digits=5, decimal_places=2)
    length_of_increased_moisture = models.DecimalField(max_digits=5, decimal_places=2)

class Plant(models.Model):
    plant_name = models.CharField(max_length=200)
    plant_type = models.CharField(max_length=200)
    plant_soil_type = models.CharField(max_length=200)
    location = models.IntegerField()
    def __str__(self):
        return self.plant_name
		
class LocationChoice(models.Model):
    plant = models.ForeignKey(Plant)
    location_choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.location_choice_text