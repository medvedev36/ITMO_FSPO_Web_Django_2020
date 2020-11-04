from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.db.models import Q, Count, F
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, DeleteView


from .models import Ride, Ticket
from .forms import TicketForm

# Create your views here.
def home(request):
    return render(request, 'tickets/home.html')

def validate_input(request):
    ticket_from = request.GET.get('from')
    ticket_to = request.GET.get('to')
    date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d')
    if not ticket_from.startswith('г. '):
        ticket_from = 'г. {}'.format(ticket_from)
    if not ticket_to.startswith('г. '):
        ticket_to = 'г. {}'.format(ticket_to)
    return ticket_from, ticket_to, date

def ride_list(request):
    try: 
        ticket_from, ticket_to, date = validate_input(request)
    except ValueError:
        return redirect('home')
    context = {}
    context['queryset'] = Ride.objects.filter(
        Q(where_from__name=ticket_from), 
        Q(where__name=ticket_to),
        Q(departure_datetime__range=(date, date + timedelta(hours=24)))
    ).annotate(ticket_count=F('bus__bus_type__people_capacity') - Count('ticket')).order_by('departure_datetime')
    return render(request, 'tickets/ride_list.html', context)


@login_required
def buy_ticket(request, ride):
    ride = get_object_or_404(Ride, id=ride)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        form.instance.user = request.user
        form.instance.ride = ride
        print(form.data.get('payment_type'))
        print(type(form.data.get('payment_type')))
        if form.is_valid():
            form.save()
            request.user.points += ride.price // 100
            request.user.save()
            return redirect('ticket-info', form.instance.id)
    else:
        form = TicketForm()
    context = {
        'ride': ride,
        'form': form
    }
    return render(request, 'tickets/confirm_purchase.html', context)


class TicketDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Ticket

    def test_func(self):
        ticket = self.get_object()
        return self.request.user == ticket.user
        
@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    context = {
        'tickets': tickets
    }
    return render(request, 'tickets/ticket_list.html', context)

class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = '/profile'

    def test_func(self):
        ticket = self.get_object()
        return self.request.user == ticket.user
