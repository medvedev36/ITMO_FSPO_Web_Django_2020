from django import forms
from .models import *


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            "id",
        ]


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            "name",
            "surname",
            "address",
        ]


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [
            "title",
            "address",
        ]


class CassetteForm(forms.ModelForm):
    class Meta:
        model = Cassette
        fields = [
            "title",
            "theme",
            "director",
            "release_date",
            "studio",
        ]


class SellingForm(forms.ModelForm):
    class Meta:
        model = CassetteSelling
        fields = [
            "cassette",
            "seller",
            "date",
            "price",
            "quantity",
            "client",
        ]


class ArrivingForm(forms.ModelForm):
    class Meta:
        model = CassetteArriving
        fields = [
            "cassette",
            "seller",
            "date",
            "price",
            "quantity",
            "provider",
        ]
