from django import forms
from django.contrib.auth import get_user_model
from planner.models import Event, Reservation

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))

    
    class Meta():
        model = User
        fields = ["username", "password"]

        widgets = {
            "password": forms.PasswordInput()
        }

class LoginForm(forms.Form):

    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))

class ReservationForm(forms.ModelForm):
    users = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    event = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))



    class Meta:
        model = Reservation
        fields = '__all__'