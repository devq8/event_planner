from django.shortcuts import render
from users.forms import LoginForm

# Create your views here.

def get_home(request):
    form = LoginForm()
    context = {"form": form}

    return render(request, "index.html",context)