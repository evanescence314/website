from django.contrib import messages
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def index(request):    
    #messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'index.html')

def rankings(request):
    return render(request, 'rankings.html')

def lettering(request):
    return render(request, 'lettering.html')

def calendar(request):
    return render(request, 'calendar.html')

def tjimo(request):
    return render(request, 'tjimo.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
