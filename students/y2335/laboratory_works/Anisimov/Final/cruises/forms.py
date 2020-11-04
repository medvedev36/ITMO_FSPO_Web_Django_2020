from django.forms import  ModelForm
from .models import Ticket, Tour
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('ownername','category',)

class FindForm(ModelForm):
    class Meta:
        model = Tour
        fields = ('motorship',)