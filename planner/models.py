from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import (MinValueValidator, MaxValueValidator) #MaxValidator not being used at the moment but will be used in future.

User = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="media/")
    number_of_seats = models.PositiveIntegerField()
    date = models.DateField()
    location = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name
        

class Reservation(models.Model):
    users = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "users"
    )

    event = models.ForeignKey(
        Event,
        on_delete = models.CASCADE,
        related_name="event",
    )

    seats = models.PositiveIntegerField(validators=[MinValueValidator(1, "Minimum reservation seats is 1 seat."),])

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"Reservation ID: {self.id}"
