from django.forms import ModelForm
from .models import Traveller, Location, TravelPlan

class TravellerForm(ModelForm):
    class Meta:
        model = Traveller
        fields = ['last_name', 'first_name', 'nationality', 'mobile_number', 'email', 'password', 'preferences']


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['country', 'city', 'name', 'language']


class TravelPlanForm(ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['travel_plan_name', 'date_from', 'date_to']
