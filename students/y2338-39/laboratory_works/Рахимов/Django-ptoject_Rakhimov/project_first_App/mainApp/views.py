from django.shortcuts import render, redirect
from .models import City, Hotel, Nomer, InfoAboutNomer, Customers, Registration, currentCusromer
from .forms import CustomersForm, CustomerFormAuto, RegistrationForm
from django.views import generic


def index(request):
    current = currentCusromer.objects.get()
    return render(request, 'mainApp/main.html', {'current': current})


def contacts(request):
    current = currentCusromer.objects.get()
    return render(request, 'mainApp/contacts.html', {'current': current})


class EconomListView(generic.ListView):
    model = Nomer
    context_object_name = "context"
    my_info = InfoAboutNomer.objects.filter(type_nomer="e")
    queryset__in = Nomer.objects.filter(info=my_info)
    template_name = "mainApp/types/econom.html"


class StandartListView(generic.ListView):
    model = Nomer
    context_object_name = "context"
    my_info = InfoAboutNomer.objects.filter(type_nomer="s")
    queryset__in = Nomer.objects.all().filter(info=my_info)
    template_name = "mainApp/types/standart.html"


class LuxListView(generic.ListView):
    model = Nomer
    context_object_name = "context"
    my_info = InfoAboutNomer.objects.all().filter(type_nomer="l")
    queryset__in = Nomer.objects.all().filter(info=my_info)
    template_name = "mainApp/types/lux.html"


class PresidentListView(generic.ListView):
    model = Nomer
    context_object_name = "context"
    my_info = InfoAboutNomer.objects.all().filter(type_nomer="p")
    queryset__in = Nomer.objects.all().filter(info=my_info)
    template_name = "mainApp/types/president.html"


def registration(request):
    error = ''
    if request.method == 'POST':
            form = CustomersForm(request.POST)
            if form.is_valid() and Customers.objects.exclude(number_passport_customer=form.cleaned_data.get
                ('number_passport_customer')):
                form.save()
                return render(request, 'mainApp/main.html')
            else:
                error = 'Некорректная форма, введите заново'

    form = CustomersForm()
    context = {'form': form,
               'error': error
    }
    return render(request, 'mainApp/registration.html', context)


def autorisation(request):
    form = CustomerFormAuto(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            customer = Customers.objects.get(number_passport_customer=form.cleaned_data.get('number_passport_customer'))
            if customer:
                currentCusromer.objects.all().delete()
                current = currentCusromer(
                    fio=customer.fio,
                    passport=customer.number_passport_customer,
                    phone=customer.number_phone_cus
                )
                current.save()
                return index(request)
            else:
                error = 'Некорректные данные, введите заново'
    form = CustomerFormAuto()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'mainApp/autorisation.html', context)


def exit(request):
    currentCusromer.objects.all().delete()
    current = currentCusromer(fio=" ", passport=1, phone=1)
    current.save()
    return index(request)


def profile(request):
    prof = currentCusromer.objects.get()
    return render(request, 'mainApp/profile.html', {'profile': prof})


def bron(request):
    form = RegistrationForm(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            customer = currentCusromer.objects.get()
            cus = Customers.objects.get(number_passport_customer=customer.passport)
            reg = Registration(
                customers=cus, nomer=form.cleaned_data.get("nomer"),
                date_entry=form.cleaned_data.get('date_entry'),
                date_exit=form.cleaned_data.get('date_exit'),
                status_nomer="z"
            )
            reg.save()
            return index(request)
        else:
            error = 'Некорректные данные, введите заново'
    form = RegistrationForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainApp/reg_number.html', context)

# Create your views here.
