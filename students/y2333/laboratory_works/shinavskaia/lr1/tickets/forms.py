from django import forms


from .models import Ticket
from .choices import PAYMENT_TYPE_CHOICE


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['payment_type']
    
    def is_valid(self):
        if self.data.get('payment_type') == '3':
            if self.instance.user.points < self.instance.ride.price:
                return False
            self.instance.user.points -= self.instance.ride.price
            self.instance.user.save()
        return super().is_valid()
