from django.shortcuts import render, redirect
from .forms import TravellerForm
from .models import Traveller

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = TravellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations')
    else:
        form = TravellerForm()

    return render(request, 'signup.html', {'form': form})

def match(request):
    return render(request, 'match.html')

def location_matcher(traveller_data, location_data):
    print(Traveller.objects.all())
