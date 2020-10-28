from django import forms
from django.contrib.auth.models import User
from .models import Vehicle


class OwnerForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'username',
            'email',
        ]

# class VehicleForm(forms.ModelForm):

#     class Meta:
#         model = Vehicle
#         fields = [
#             'model',
#             'brand',
#             'color',
#             'license_plate',
#         ]