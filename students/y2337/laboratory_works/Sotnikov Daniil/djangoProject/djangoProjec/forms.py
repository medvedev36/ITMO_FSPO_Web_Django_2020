from django import forms
from .models import *


class ShipForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = [
            "ship_id",
            "name",
            "release",
            'deadline',
            'team',
            'economy_price',
            'business_price',
            'luxury_price'
        ]


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = [
            'route_id',
            'name',
            'days',
            'stops'
        ]


class ExcForm(forms.ModelForm):
    class Meta:
        model = Excursion
        fields = [
            'excursion_id',
            'e_ship_id',
            'e_route_id',
            'departure',
            'economy_pass',
            'business_pass',
            'luxurious_pass'
        ]

class ExcEditForm(forms.ModelForm):
    class Meta:
        model = Excursion
        fields = [
            'e_ship_id',
            'e_route_id',
            'departure',
            'economy_pass',
            'business_pass',
            'luxurious_pass'
        ]
