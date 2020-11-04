from django import forms
from .models import *


class AddOwner(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "name",
            "surname",
            "birthday",
        ]


#Удалить
class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = [
            "title",
            "description",
        ]