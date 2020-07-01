from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["address", "book", "count", "first_name", "last_name", "patronymic", "phone", "email"]
