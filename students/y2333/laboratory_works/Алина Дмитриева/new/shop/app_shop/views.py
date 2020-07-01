from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app_shop.models import *
from .forms import *


def base(request):
    context = {'data_c': Сassette.objects.all(), 'data_s': Seller.objects.all(), 'data_a': Admission.objects.all()}
    return render(request, 'base.html', context)


def sort(request, theme):
    context = {'data_c': Сassette.objects.all().filter(theme__exact=theme), 'data_s': Seller.objects.all(), 'data_a': Admission.objects.all()}
    return render(request, 'sort.html', context)


def search(request):
    context = {'data_c': Сassette.objects.all()}
    return render(request, 'search.html', context)


def account(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        context = {'data_u': user, 'data_c': Сassette.objects.all(), 'data_s': Seller.objects.all(),
                   'data_sg': Selling.objects.all()}
    except User.DoesNotExist:
        raise Http404("Пользователя не сущетсвует")
    return render(request, 'account.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.photo = form.cleaned_data.get('photo')
            user.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def selling(request, user_id, cassette_id):
    context = {}
    form = Selling_form(request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect('/base')
    context['data_u'] = User.objects.get(pk=user_id)
    context['data_c'] = Сassette.objects.get(pk=cassette_id)
    context['data_s'] = Seller.objects.all()
    context['data_a'] = Admission.objects.all()
    context['form'] = form
    return render(request, "selling.html", context)


# def sale(request, id_cassette, seller_id):
#     Admission.objects.filter(id_seller=seller_id, id_cassette=id_cassette).update(quantity-= 1)

    # if request.method == 'POST':
    #     form = Selling_form(request.POST or None)
    #     # form.instance.client = request.user
    #     #form.instance.fuel_in_station = get_object_or_404(FuelInStation, fuel_id=fuel, station_id=station)
    #     if form.is_valid():
    #         form.save()
    #     return base(request)
    # else:
    #     context = {}
    #     form = Selling_form(request.POST or None)
    #     context['data_u'] = User.objects.get(pk=user_id)
    #     context['data_c'] = Сassette.objects.get(pk=cassette_id)
    #     context['data_s'] = Seller.objects.all()
    #     context['data_a'] = Admission.objects.all()
    #     context['form'] = form
    # return render(request, "selling.html", context)


def cassette_add(request):
    context = {}
    form = Сassette_form(request.POST or None)
    context['data_c'] = Сassette.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "cassette_add.html", context)


def cassette_delete(request, cassette_id):
    try:
        c = Сassette.objects.get(id=cassette_id)
        c.delete()
        return redirect('/base')
    except Сassette.DoesNotExist:
        return HttpResponseNotFound("<h2>Фильм не найден</h2>")


def show_for_delete(request):
    context = {'data_c': Сassette.objects.all()}
    return render(request, 'cassette_delete.html', context)
