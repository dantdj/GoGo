from django.shortcuts import render, redirect
from .forms import TravellerForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = TravellerForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('/')
    else:
        form = TravellerForm()

    return render(request, 'signup.html', {'form': form})

def match(request):
    return render(request, 'match.html')
