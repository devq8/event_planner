from django.contrib import admin
from planner.models import Event
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields= ("created_at", "modified_at")

    