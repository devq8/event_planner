from tabnanny import verbose
from django.db import models


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    number_of_seats = models.IntegerField()
    number_of_booked_seats = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name

class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    event = models.ForeignKey(
        Event,
        on_delete = models.CASCADE,
        related_name="event",
    )