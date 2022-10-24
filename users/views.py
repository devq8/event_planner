import os
from django.shortcuts import render,redirect
from users.forms import RegistrationForm, LoginForm
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
    events_list = Event.objects.all()
    path = settings.MEDIA_ROOT
    
    new_list = []
    for event in events_list:
        img_list = (f"{path}/{event.image}")
        new_list.append({
            "name": event.name,
            "image": img_list,
            "date": event.date,
        })
    context = {"events": new_list}
    print(context)
    return render (request, "events_list.html", context)