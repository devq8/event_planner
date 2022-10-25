from django.contrib import admin
from planner.models import Event, Reservation
# Register your models here.


@admin.register(Event, Reservation)
class EventAdmin(admin.ModelAdmin):
    readonly_fields= ("created_at", "modified_at")

class ReservationAdmin(admin.ModelAdmin):
    readonly_fields= ("created_at", "modified_at")

    