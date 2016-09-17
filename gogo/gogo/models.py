from django.db import models


class Traveller(models.Model):
    traveller_ID = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=30)
    preferences = models.CharField(max_length=200)


class Location(models.Model):
    location_ID = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)


class TravelPlan(models.Model):
    travel_plan_ID = models.IntegerField(primary_key=True)
    tavel_plan_name = models.CharField(max_length=200)
    traveller_ID = models.ForeignKey(Traveller)
    location_ID = models.ForeignKey(Location)
    date_from = new DateTimeField()
    date_to = new DateTimeField()
