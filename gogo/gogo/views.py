from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import TravellerForm
from .models import Traveller

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = TravellerForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            user_list = location_match(data)
            email_users(user_list)
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

    user_list = []
    for item in db_contents:
        print(item.first_name, item.last_name, item.email)
        user_list.append(item.email)
    user_list.append(data.email)
    return user_list

def email_users(user_list):
    email = EmailMessage("New match!", "You've been matched with the users that were also sent this message, talk to them!", to=user_list)
    email.send()
