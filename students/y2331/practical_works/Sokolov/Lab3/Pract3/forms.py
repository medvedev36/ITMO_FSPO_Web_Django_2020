from .models import User
from django import forms

class UserForm(forms.ModelForm):
     class Meta:
         model = User
         fields = [
             "people",
             "first_name",
             "second_name"
         ]