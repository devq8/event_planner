from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import datetime
from django.shortcuts import render, redirect
from planner.forms import ReservationForm, CreateEventForm
from planner.models import Event, Reservation
from django.utils import timezone

User = get_user_model()

def get_home(request):
    return render(request, "index.html")

def get_events(request):
    if request.user.is_staff:   
        events_list = Event.objects.all()
        new_events_list = []
        for event in events_list:
            reservations = Reservation.objects.filter(event=event.id)
            total_reservations = 0
            for reservation in reservations:
                total_reservations += reservation.seats

            new_events_list.append({
                "id": event.id,
                "name": event.name,
                "image": event.image,
                "date": event.date,
                "available_seats": (event.number_of_seats - total_reservations),
                "total_seats": event.number_of_seats,
            }) 
        
        context = {"events": new_events_list}
    else:
        upcoming_events = Event.objects.filter(date__gt=datetime.datetime.now())
        new_upcoming_events = []

    
        for event in upcoming_events:
            reservations = Reservation.objects.filter(event=event.id)
            total_reservations = 0
            for reservation in reservations:
                total_reservations += reservation.seats

            new_upcoming_events.append({
                "id": event.id,
                "name": event.name,
                "image": event.image,
                "date": event.date,
                "available_seats": (event.number_of_seats - total_reservations),
                "total_seats": event.number_of_seats,
            })
        
        context = {"events": new_upcoming_events}

    return render (request, "events_list.html", context)

def get_event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    
    
    context = {
        "event": {
            "id": event.id,
            "name": event.name,
            "date": event.date,
            "location": event.location,
            "number_of_seats": event.number_of_seats,
            "image": event.image,
        }
    }

    return render(request, "event_detail.html", context)

@login_required
def create_reservation(request, event_id):
    event = Event.objects.get(id=event_id)
    reservations = Reservation.objects.filter(event=event_id)
    total_reservations = 0
    for reservation in reservations:
        total_reservations += reservation.seats
    
    available_seats = event.number_of_seats - total_reservations

    form = ReservationForm(initial={
        "users": request.user.id,
        "event": event_id,
    })
    
    # if request.POST.get("seats") > available_seats:
    #     print("Issue")
    # else:
    #     print("No issue!")
    
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if int(request.POST.get("seats")) <= (available_seats):
            if form.is_valid():
                form.save()
                return redirect("events-list")

    context = {
        "form": form
    }

    return render(request, "reserve.html", context)

@login_required
def create_event(request):
    form = CreateEventForm()
    if request.method == "POST":
        form = CreateEventForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
        
            return redirect("events-list")
        
    context = {
        "form": form,
    }

    return render(request, "create_event.html", context)