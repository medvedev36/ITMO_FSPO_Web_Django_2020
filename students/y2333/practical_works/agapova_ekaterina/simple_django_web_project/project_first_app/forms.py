from django import forms
from .models import Owner


# creating a form
class OwnersForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "firstName",
            "secondName",
            "user"
        ]