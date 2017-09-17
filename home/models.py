from django.db import models
from geoposition.fields import GeopositionField
from django.utils import timezone

# Create your models here.

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.description


class Event(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.FileField()
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + ' - by ' + self.organisation.name


# anytime you make a change to the database
# python manage.py makemigrations
# python manage.py migrate

# Database API Shell

class Location(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    position = GeopositionField()

    def __str__(self):
        return self.event.name + ' at ' + self.address + '(' + self.city + ')'

