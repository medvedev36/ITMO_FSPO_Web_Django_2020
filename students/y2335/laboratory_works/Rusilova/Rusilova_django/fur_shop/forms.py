from django.forms import ModelForm
from .models import *


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = []


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']