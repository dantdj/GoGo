from django.shortcuts import render, redirect
from .forms import TravellerForm, LocationForm, TravelPlanForm
from .models import Traveller
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = TravellerForm(request.POST)
        user = User.objects.create_user(request.POST['first_name'], request.POST['email'],request.POST['password'])
        user.save()
        if form.is_valid():
            form.save()
            return redirect('locations')
    else:
        form = TravellerForm()

    return render(request, 'signup.html', {'form': form})
def login(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('success.html')
    return render(request,'login.html',{'form': form})
def locations(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('travelplan')
    else:
        form = LocationForm()

    return render(request, 'locations.html', {'form': form})

def travelplan(request):
    if request.method == "POST":
        form = TravelPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TravelPlanForm()

    return render(request, 'travelplan.html', {'form': form})

def match(request):
    return render(request, 'match.html')

def location_matcher(traveller_data, location_data):
    print(Traveller.objects.all())
