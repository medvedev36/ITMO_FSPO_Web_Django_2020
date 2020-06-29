from django import forms
from .models import Clients


class OrderForm(forms.ModelForm):
    Count = forms.IntegerField()

    class Meta:
        model = Clients
        fields = ('client_first_name',
                  'client_last_name',
                  'client_address',
                  'client_city',
                  'client_phone_number',
                  'client_credit_number')
