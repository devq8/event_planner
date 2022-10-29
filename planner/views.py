import datetime
from django.shortcuts import render, redirect
from planner.forms import ReservationForm, CreateEventForm
from planner.models import Event
from django.utils import timezone

# Create your views here.

def get_home(request):
    return render(request, "index.html")

def get_events(request):

    # if request.user.is_anonymous:
    #     return redirect("login")


    events_list = Event.objects.all()


    new_list = []
    
    for event in events_list:

        today = datetime.date(timezone.now().year,timezone.now().month,timezone.now().day)
        event_date = datetime.date(event.date.year,event.date.month,event.date.day)

        days_different = event_date - today

        days_message = ""
        passed = False

        if days_different.days >= 0 :
            days_message = f"{days_different.days} days to go."
        else:
            days_message = f"Passed!"
            passed = True

        if request.user.is_staff:
            new_list.append({
                "id": event.id,
                "name": event.name,
                "image": event.image,
                "date": event.date,
                "location": event.location,
                "available_seats": (event.number_of_seats),
                "total_seats": (event.number_of_seats),
                "days_to_go": days_message ,
                "passed": passed,
            })
        else:
            if not passed:
                new_list.append({
                    "id": event.id,
                    "name": event.name,
                    "image": event.image,
                    "date": event.date,
                    "location": event.location,
                    "available_seats": (event.number_of_seats),
                    "total_seats": (event.number_of_seats),
                    "days_to_go": days_message ,
                    "passed": passed,
                })

    context = {"events": new_list}


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


def create_reservation(request):
    form = ReservationForm()
    
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("events-list")

    context = {
        "form": form
    }

    return render(request, "reserve.html", context)

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