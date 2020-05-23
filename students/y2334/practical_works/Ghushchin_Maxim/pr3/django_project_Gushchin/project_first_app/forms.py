from django import forms
from project_first_app.models import *


class PersonForm(forms.ModelForm):
    class Meta:

        model = Person
        fields = 'first_name', 'last_name', 'date'


