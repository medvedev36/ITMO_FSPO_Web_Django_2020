from django import forms
from .models import CarOwner
from .models import DriversLicense


# creating a form
class GeeksForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner

        # specify fields to be used
        fields = [
            "name",
            "surname",
            "birthDate",

        ]
