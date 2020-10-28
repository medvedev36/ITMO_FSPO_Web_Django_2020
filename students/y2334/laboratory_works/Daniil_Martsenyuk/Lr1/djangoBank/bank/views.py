from django.shortcuts import render, redirect
from bank.forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'bank/home.html')


def registration_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/registration_form.html', {'form': form})


@login_required
def user_profile_view(request):
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ClientForm(instance=client)

    context = {
        'form': form,
    }
    return render(request, 'accounts/user_profile_form.html', context)


@login_required
def create_account(request):
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            account = Account.objects.last()
            client.account.add(account)
            return redirect('user_profile')
    else:
        form = AccountForm()

    return render(request, 'bank/create_account_form.html', {'form': form})


def user_account_view(request):
    client = Client.objects.get(user=request.user)
    return render(request, 'bank/user_account.html', {'client': client})


def create_contract_view(request):
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            contract = Contract.objects.last()
            client.contract_code.add(contract)
            return redirect('user_profile')
    else:
        form = ContractForm()

    return render(request, 'bank/create_contract_form.html', {'form': form})


def user_contract_view(request):
    client = Client.objects.get(user=request.user)
    return render(request, 'bank/user_contract.html', {'client': client})


def send_report(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SupportForm()
    return render(request, 'support.html', {'form': form})
