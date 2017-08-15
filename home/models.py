from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.description


class Event(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.FileField()

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
    position = GeopositionField(blank=True)

