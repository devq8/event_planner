from django import forms
from planner.models import Event, Reservation
import datetime



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

    date = forms.DateField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "date",
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