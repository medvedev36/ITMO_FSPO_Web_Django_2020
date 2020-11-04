from django.shortcuts import render, get_object_or_404, redirect
from cruises.models import Motorship, Tour, Ticket, Sailor
from cruises.forms import TicketForm, FindForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

class RegisterView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/accounts/login"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterView, self).form_valid(form)

# Create your views here.
def motorship_list(request):
    motorships = Motorship.objects.all()
    return  render(request, "cruises/motorship_list.html", {"motorships": motorships})

# def login(request):
#     return  render(login, "registration/login.html")

def find(request):
    if request.method == "POST":
        form = FindForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return redirect("/tour/" + str(form.motorship.id))
    else:
        form = FindForm()
    return render(request, "cruises/find.html", {"form" : form})

def sailor_list(request):
    sailors = Sailor.objects.all()
    return  render(request, "cruises/sailor_list.html", {"sailors": sailors})

def thanks(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    return  render(request, "cruises/thanks.html", {"ticket" : ticket})

def tickets(request):
    tickets = Ticket.objects.all().filter(user_id = request.user.id)
    return  render(request, "cruises/tickets.html", {"tickets" : tickets})

def tour_list(request):
    tours = Tour.objects.all()
    return  render(request, "cruises/tours.html", {"tours" : tours })

def tour(request, pk):
    tours = Tour.objects.all().filter(motorship_id = pk)
    return  render(request, "cruises/tour.html", {"tours" : tours })

def remove(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    ticket.delete()
    return  render(request, "cruises/remove.html", {"ticket" : ticket})

def tour_buy(request, pk):
    tour = get_object_or_404(Tour, id=pk)

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.ticket_id = 0
            form.user_id = request.user.id
            form.category = form.category
            form.tour = tour
            form.save()
            return redirect("/thanks/" + str(form.id))
    else:
        form = TicketForm()
    return render(request, "cruises/buy.html", {"tour" : tour, "form" : form})