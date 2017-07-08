from django.db import models

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
    image = models.CharField(max_length=5000)

    def __str__(self):
        return self.name + ' - by ' + self.organisation.name


# anytime you make a change to the database
# python manage.py makemigrations
# python manage.py migrate

# Database API Shell
#