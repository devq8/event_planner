import datetime
from django.utils import timezone
from django.shortcuts import render,redirect
from users.forms import CreateEventForm, RegistrationForm, LoginForm, ReservationForm
from django.contrib.auth import login, logout, login, authenticate
from planner.models import Event
from django.conf import settings


def register_user(request):
    # Create new instance of RegisterationForm.
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #commit=False means to pause the saving process
            user.set_password(user.password) #To hide the password field in the form
            user.save() #Save to db
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                )
            login(request, user)
            return redirect("home") #redirect to 'home' page
    context = {"form": form}
    return render(request, "register.html", context)

def logout_user(request):
    logout(request)
    return redirect("home")

def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home")
    context = {"form": form}
    return render (request, "login.html", context)

def get_events(request):

    if request.user.is_anonymous:
        return redirect("login")


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
        print("Before if")
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("events-list")
        print("After if")
    context = {
        "form": form,
    }

    return render(request, "create_event.html", context)