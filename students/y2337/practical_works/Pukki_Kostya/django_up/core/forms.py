from django import forms
from .models import Owner, Car

class OwnerForm(forms.ModelForm):
  class Meta:
    model = Owner
    fields = {
      "first_name": forms.TextInput(),
      "last_name": forms.TextInput(),
      "birthday": forms.DateInput()
    }


class CarForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = [
      "id", "brand", "model", "color", "num"
    ]