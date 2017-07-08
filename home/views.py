from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Organisation, Event

# Create your views here.

# Views takes request and returns hhtp response

def index(request):

    all_orgs = Organisation.objects.all()
    all_events = Event.objects.all()

    context = {
        'all_orgs': all_orgs,
        'all_events': all_events,

    }
    return render(request, 'home/index.html', context)


