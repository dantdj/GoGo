from django.db import models


class Traveller(models.Model):
    traveller_ID = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=80)
    destination_city = models.CharField(max_length=150)
    destination_country = models.CharField(max_length=150)
    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField()
    def __str__(self):
        return self.last_name
