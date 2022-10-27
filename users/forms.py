from email.mime import image
from django import forms
from django.contrib.auth import get_user_model
from planner.models import Event, Reservation
import datetime

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
    seats = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = Reservation
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateEventForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        }))

    # ------- Needs to be fixed -------                         [ works fine while commented ]
    # image = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "form-control",
    #     "type": "file"
    #     }))

    number_of_seats = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        }))

    date = forms.DateField(widget=DateInput(attrs={
        "class": "form-control",
        }))
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    location = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        }))


    class Meta:
        model = Event
        fields = ['name', 'image', 'number_of_seats', 'date', 'location']