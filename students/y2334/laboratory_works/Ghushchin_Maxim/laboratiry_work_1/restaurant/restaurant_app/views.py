from django.shortcuts import render, redirect
from restaurant_app.forms import *
from django.contrib.auth.decorators import login_required
from restaurant_app.models import *
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/registration_form.html', {'form': form})


@login_required
def main_page(request):
    return render(request, 'accounts/main_page.html')


@login_required
def view_menu(request):
    dishes = Dishes.objects.all()
    context = {
        'dishes': dishes,
    }
    return render(request, 'accounts/menu.html', context)


@login_required
def view_tables(request):
    tables = Table.objects.all()
    current_user = request.user
    context = {
        'tables': tables,
        'current_user': current_user,
    }
    return render(request, 'accounts/tables.html', context)


@login_required
def operation_with_reservation(request, pk):

    client = Client.objects.get(user=request.user)

    if client.phone is None:
        messages.success(request, "Для бронирования столика вам необходимо ввести "
                                  "свой номер телефона, чтобы мы могли с вами связаться!")
        return redirect('client_order')
    all_reservation = Reservation.objects.all()
    for res in all_reservation:
        if res.client == request.user:
            messages.error(request, "Вы уже забронировали столик на сегодня!")
            return redirect('tables')

    reservation = Reservation.objects.get(pk=pk)
    if reservation.available:
        reservation.available = False
        reservation.client = request.user
    else:
        reservation.available = True
    reservation.save()
    return redirect('tables')


@login_required
def client_order(request):
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('tables')
    else:
        form = ClientForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/client_form.html', context)


@login_required
def client_help(request):
    return render(request, 'accounts/client_help.html')


@login_required
def view_menu(request):
    dishes = Dishes.objects.all()
    try:
        client = Client.objects.get(user=request.user)
        order = Orders.objects.get(client=client)
        context = {
            'dishes': dishes,
            'order': order,
        }
    except:
        context = {
            'dishes': dishes,
        }
    return render(request, 'accounts/menu.html', context)


@login_required
def add_order(request, pk):
    client = Client.objects.get(user=request.user)
    dish = Dishes.objects.get(pk=pk)
    try:
        client_order = Orders.objects.get(client=client)
        client_order.dishes.add(dish)
        client_order.save()
    except:
        client_order = Orders(client=client)
        client_order.save()
        client_order.dishes.add(dish)
        client_order.save()
    return redirect('view_cart')


@login_required
def remove_order(request, pk):
    client = Client.objects.get(user=request.user)
    dish = Dishes.objects.get(pk=pk)
    client_order = Orders.objects.get(client=client)
    client_order.dishes.remove(dish)
    client_order.save()
    return redirect('view_cart')


@login_required
def confirmed_order(request):
    client = Client.objects.get(user=request.user)
    cart = Orders.objects.get(client=client)
    reservation = Reservation.objects.get(client=request.user)
    total_price = 0
    for dish in cart.dishes.all():
        total_price += dish.price
    context = {
        'cart': cart,
        'total_price': total_price,
        'reservation': reservation,
    }
    return render(request, 'accounts/confirmed_order.html', context)


@login_required
def view_cart(request):
    client = Client.objects.get(user=request.user)
    cart = Orders.objects.get(client=client)
    if cart.check == True:
        return redirect('confirmed_order')
    total_price = 0
    for dish in cart.dishes.all():
        total_price += dish.price
    context = {
        'cart': cart,
        'total_price': total_price,
    }
    return render(request, 'accounts/cart.html', context)


@login_required
def send_review(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_ty')
    else:
        form = SupportForm()
    return render(request, 'accounts/support_form.html', {'form': form})


@login_required
def view_ty(request):
    return render(request, 'accounts/ty.html')


@login_required
def close_order(request):
    client = Client.objects.get(user=request.user)
    order = Orders.objects.get(client=client)
    order.check = True
    order.save()
    messages.success(request, "Вы успешно оформили заказ! ")
    return redirect('view_cart')


@login_required
def cancel_order(request):
    client = Client.objects.get(user=request.user)
    order = Orders.objects.get(client=client)
    order.check = False
    order.save()
    messages.error(request, "Вы отменили свой заказ! ")
    return redirect('view_cart')

