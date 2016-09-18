from django.shortcuts import render, redirect
from .forms import TravellerForm
from .models import Traveller

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = TravellerForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            location_match(data)
            form.save()
            return redirect('/')
    else:
        form = TravellerForm()

    return render(request, 'signup.html', {'form': form})

def match(request):
    return render(request, 'match.html')

def location_match(data):
    db_contents = Traveller.objects.all()
    db_contents = db_contents.filter(destination_city=data.destination_city)
    db_contents = db_contents.filter(destination_country=data.destination_country)
    db_contents = db_contents.filter(arrival_date__lte=data.departure_date)
    db_contents = db_contents.filter(departure_date__gte=data.arrival_date)
    for item in db_contents:
        print(item.first_name, item.last_name, item.email)
