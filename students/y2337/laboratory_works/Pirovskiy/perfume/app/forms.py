from django import forms
from .models import *


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "id",
        ]


class MacklerForm(forms.ModelForm):
    class Meta:
        model = Mackler
        fields = [
            "idMac",
            "surMac",
            "adrMac",
        ]


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['expProd'].label = "Срок годности продукта"

    expProd = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Product
        fields = [
            "nameProd",
            "varProd",
            "priceProd",
            "idComp",
            "expProd",
        ]
