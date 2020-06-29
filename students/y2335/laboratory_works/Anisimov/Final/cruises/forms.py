from django.forms import  ModelForm
from .models import Ticket, Tour

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('ownername','category',)

class FindForm(ModelForm):
    class Meta:
        model = Tour
        fields = ('motorship',)