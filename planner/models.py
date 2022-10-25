from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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

    users = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "users"
    )

    def __str__(self) :
        return f"Reservation ID: {self.id}"