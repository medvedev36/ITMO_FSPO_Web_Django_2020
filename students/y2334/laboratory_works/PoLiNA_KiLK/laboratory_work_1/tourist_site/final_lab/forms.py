from django import forms
from .models import Routes, Buses, Staff, Ways, Cities


class RoutesForm(forms.ModelForm):
    class Meta:
        model = Routes

        fields = ["Name", "Start", "Finish", "Duration"]


class BusesForm(forms.ModelForm):
    class Meta:
        model = Buses
        fields = ["Number", "Name", "Total_run"]


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["Experience", "Category", "Address", "Birth_year", "Number_b", "Second_name"]


class WaysForm(forms.ModelForm):
    class Meta:
        model = Ways
        fields = ["Start_date", "Finish_date", "Passengers", "Ticket_cost", "Name", "Number"]


class CitiesForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ["Name", "Towns"]