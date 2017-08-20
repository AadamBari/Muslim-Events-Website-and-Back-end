from rest_framework import serializers
from .models import Organisation
from .models import Event
from .models import Location

# serializer means convert model/python object to data that can be saved or transferred

class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        # fields = ('name', 'description') # The model attributes you want to return
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

