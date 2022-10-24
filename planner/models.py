from django.db import models


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True)
    number_of_seats = models.IntegerField()
    number_of_booked_seats = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)