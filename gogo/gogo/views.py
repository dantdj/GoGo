from django.http import HttpResponse

def index(request):
    return HttpResponse("You've got the index page!")

def signup(request):
    return HttpResponse("You've got the signup page!")

def match(request):
    return HttpResponse("Here's your new travelling partner/s!")
