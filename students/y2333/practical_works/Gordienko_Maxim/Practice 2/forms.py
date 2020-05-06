from .models import User
from django import forms

class UserForm(forms.ModelForm):
     class Meta:
         # specify model to be used
         model = User

         # specify fields to be used
         fields = [
             "first_name",
             "second_name",
         ]