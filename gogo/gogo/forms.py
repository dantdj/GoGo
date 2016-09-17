from django.forms import ModelForm
from models import Traveller, Location, TravelPlan

class TravellerForm(ModelForm):
    class Meta:
        model = Traveller
        fields = ['traveller_ID', 'last_name', 'first_name', 'nationality', 'mobile_number', 'email', 'password', 'preferences']


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['location_ID', 'country', 'city', 'name', 'language']


class TravelPlanForm(ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['travel_plan_ID', 'travel_plan_name', 'traveller_ID', 'location_ID', 'date_from', 'date_to']
