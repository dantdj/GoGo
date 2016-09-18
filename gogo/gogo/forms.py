from django.forms import ModelForm
from .models import Traveller

class TravellerForm(ModelForm):
    class Meta:
        model = Traveller
        fields = ['first_name', 'last_name', 'nationality', 'mobile_number', 'email', 'destination_city', 'destination_country', 'arrival_date', 'departure_date']
