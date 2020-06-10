from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q

from .forms import *
from .models import *


def users_list(request):
    context = {"users": User.objects.all()}
    return render(request, 'myapp/users_list.html', context)


def rates_list(request):
    context = {"rates": Rate.objects.all()}
    return render(request, 'myapp/rates_list.html', context)


def cashes_list(request):
    context = {"cashes": CashInformation.objects.all()}
    return render(request, 'myapp/cashes_list.html', context)


def calls_list(request):
    context = {"calls": CallInformation.objects.all()}
    return render(request, 'myapp/calls_list.html', context)


def users_calls_list(request):
    context = {"users_calls": UserCall.objects.all()}
    return render(request, 'myapp/users_calls_list.html', context)


def certain_user(request, login):
    try:
        context = Account.objects.get(login=login)
    except Account.DoesNotExist:
        raise Http404("Account doesn't exist!")
    return render(request, 'myapp/certain_user.html', {'certain_user': context})


def autentification(request):
    if request.method == "POST":
        inp_login = request.POST.get("login")
        password = request.POST.get("password")
        try:
            profile = Account.objects.get(login=inp_login)
        except Account.DoesNotExist:
            raise Http404("Account doesn't exist!")
        if profile.password == password:
            return certain_user(request, inp_login)
            # return render(request, 'myapp/certain_user.html', {'certain_user': profile})
        else:
            autentification_form = AutentificationForm()
            return render(request, 'myapp/autentification_form.html', {"form": autentification_form})

    else:
        autentification_form = AutentificationForm()
        return render(request, 'myapp/autentification_form.html', {"form": autentification_form})


# class AccountCreate(View):
#     def get(self, request):
#         form = AutentificationForm()
#         return render(request, 'myapp/account_create.html', context={'form': form})
#
#     def post(self, request):
#         bound_form = AutentificationForm(request.POST)
#
#         if bound_form.is_valid():
#             new_account = bound_form.save()
#             return redirect(new_account)
#         return render(request, 'myapp/account_create.html', context={'new_account': bound_form})

def account_create(request):
    context = {}
    form = AutentificationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "myapp/account_create.html", context)


def certain_user_rates(request, login):
    try:
        context = Account.objects.get(login=login)
    except Account.DoesNotExist:
        raise Http404("Account doesn't exist!")
    try:
        user = User.objects.get(account__login=login)
    except User.DoesNotExist:
        context = {'login': login}
        return render(request, 'myapp/certain_user_rates.html', context)
    rate = Rate.objects.filter(callinformation__users=user)
    context = {'certain_user_rates': rate, 'login': login}
    return render(request, 'myapp/certain_user_rates.html', context)


def certain_user_calls(request, login):
    try:
        context = Account.objects.get(login=login)
    except Account.DoesNotExist:
        raise Http404("Account doesn't exist!")
    try:
        user = User.objects.get(account__login=login)
    except User.DoesNotExist:
        context = {'login': login}
        return render(request, 'myapp/certain_user_calls.html', context)
    call = CallInformation.objects.filter(usercall__user=user)
    context = {'certain_user_calls': call, 'login': login}
    return render(request, 'myapp/certain_user_calls.html', context)


def certain_user_information(request, login):
    try:
        context = Account.objects.get(login=login)
    except Account.DoesNotExist:
        raise Http404("Account doesn't exist!")
    try:
        user = User.objects.get(account__login=login)
    except User.DoesNotExist:
        context = {'login': login}
        return render(request, 'myapp/certain_user_information.html', context)
    context = {'user': user, 'login': login}
    return render(request, 'myapp/certain_user_information.html', context)


def certain_user_binding(request, login):
    try:
        context = Account.objects.get(login=login)
    except Account.DoesNotExist:
        raise Http404("Account doesn't exist!")
    if request.method == 'POST':
        account = Account.objects.get(login=login)
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
        context = {"form": form, 'login': login}
    else:
        form = AccountForm()
        context = {"form": form, 'login': login}
    return render(request, "myapp/certain_user_binding.html", context)


def certain_user_cash(request, login):
    try:
        context = Account.objects.get(login=login)
    except Account.DoesNotExist:
        raise Http404("Account doesn't exist!")
    try:
        user = User.objects.get(account__login=login)
    except User.DoesNotExist:
        context = {'login': login}
        return render(request, 'myapp/certain_user_cash.html', context)
    cash = CashInformation.objects.get(user=user)
    context = {'certain_cash': cash, 'login': login}
    return render(request, "myapp/certain_user_cash.html", context)


def pay_for_calls(request, login):
    try:
        context = Account.objects.get(login=login)
    except Account.DoesNotExist:
        raise Http404("Account doesn't exist!")
    user = User.objects.get(account__login=login)
    not_paid_calls = UserCall.objects.filter(user=user).filter(is_paid=0)
    now = datetime.now()
    debt_sum = 0
    for row in not_paid_calls:
        debt_sum += row.call.price
    not_paid_calls.update(pay_date=now)
    UserCall.objects.filter(user=user).filter(is_paid=0)
    not_paid_calls.update(is_paid=1)
    cash = CashInformation.objects.get(user=user)
    user_cash = cash.balance
    CashInformation.objects.filter(user=user).update(balance=user_cash - debt_sum)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
