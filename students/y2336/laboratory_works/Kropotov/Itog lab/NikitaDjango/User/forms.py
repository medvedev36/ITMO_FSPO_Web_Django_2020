from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from Core.models import Purchase


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'address', 'phone', 'img', 'password1', 'password2']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AddFundsForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['balance']
    
    def is_valid(self):
        return int(self.data['balance']) > 0


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['amount']
    
    def is_valid(self):
        return float(self.data['amount']) > 0
