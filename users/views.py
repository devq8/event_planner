from django.shortcuts import render,redirect
from users.forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, login, authenticate, get_user_model

User = get_user_model()

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
                return redirect("home") #redirect to 'home' page
    context = {"form": form}
    return render (request, "login.html", context)

def get_profile_details(request):
    print(request.user)
    user = User.objects.get(username=request.user)
    context = {
        "profile": {
            "username": user.username,
        }
    }

    return render(request, "profile_details.html", context)

def update_profile(request):
    # user = User.objects.get(request.username)
    # user.set_password('request.password')
    pass