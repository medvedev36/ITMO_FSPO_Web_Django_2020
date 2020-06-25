from django.shortcuts import render, get_object_or_404, redirect
from cruises.models import Motorship, Tour, Ticket, Sailor
from cruises.forms import TicketForm

# Create your views here.
def motorship_list(request):
    motorships = Motorship.objects.all()
    return  render(request, "cruises/motorship_list.html", {"motorships": motorships})

def sailor_list(request):
    sailors = Sailor.objects.all()
    return  render(request, "cruises/sailor_list.html", {"sailors": sailors})

def thanks(request):
    return  render(request, "cruises/thanks.html")

def tour_list(request):
    tours = Tour.objects.all()
    return  render(request, "cruises/tours.html", {"tours" : tours })

def tour_buy(request, pk):
    tour = get_object_or_404(Tour, id=pk)

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.ticket_id = 0
            form.category = form.category
            form.tour = tour
            form.save()
            return redirect("/thanks/")
    else:
        form = TicketForm()


    return render(request, "cruises/buy.html", {"tour" : tour, "form" : form})