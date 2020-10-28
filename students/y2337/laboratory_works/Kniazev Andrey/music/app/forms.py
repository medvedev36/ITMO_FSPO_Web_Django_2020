from django import forms
from .models import *


class DiskForm(forms.ModelForm):
    class Meta:
        model = Disk
        fields = [
            "idMusic",
            "incomeCost",
            "idProducer",
        ]


class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = [
            "name",
            "country",
        ]


class AuthorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dateOfBirth'].label = "Дата рождения"

    dateOfBirth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Author
        fields = [
            "name",
            "dateOfBirth",
        ]


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = [
            "idAuthor",
            "musicName",
        ]

