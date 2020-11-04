from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "first_name",
            "second_name",
            "license_number",
            "gender",
            "passport_ID",
            "server_user"
        ]
