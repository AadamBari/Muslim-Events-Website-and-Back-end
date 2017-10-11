from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Organisation, Event, Location
from .serializers import OrganisationSerializer, EventSerializer, LocationSerializer
from django.core.exceptions import ObjectDoesNotExist

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

def organisations(request):

    all_orgs = Organisation.objects.all()
    all_events = Event.objects.all()

    context = {
        'all_orgs': all_orgs,
        'all_events': all_events,

    }
    return render(request, 'home/organisations.html', context)

def about(request):

    return render(request, 'home/aboutus.html')

def detail(request, event_id):

    event = Event.objects.get(id__exact=event_id)

    try:
        location = Location.objects.get(event=event_id)
    except ObjectDoesNotExist:
        location = None

    context = {
        'event': event,
        'location': location,
    }

    return render(request, 'home/detail.html', context)

def orgdetail(request, org_id):

    org = Organisation.objects.get(id__exact=org_id)

    context = {
        'org': org,
    }

    return render(request, 'home/orgdetail.html', context)


# List all Organisations
class OrganisationList(APIView):

    def get(self, request):
        orgs = Organisation.objects.all()
        serializer = OrganisationSerializer(orgs, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# List all Events
class EventList(APIView):

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# List all Locations
class LocationList(APIView):

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self):
        pass
