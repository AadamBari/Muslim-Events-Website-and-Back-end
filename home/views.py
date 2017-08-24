from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Organisation, Event, Location
from .serializers import OrganisationSerializer, EventSerializer, LocationSerializer

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

def detail(request, event_id):

    return render(request, 'home/detail.html')


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
