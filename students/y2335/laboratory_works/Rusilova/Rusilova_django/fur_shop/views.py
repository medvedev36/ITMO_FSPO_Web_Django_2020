
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from .forms import *
from .models import *
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from django.db.models import  Count,  Sum
# Create your views here.



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/home/")

class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login"
    template_name = "registration/register.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

class HomePageView(TemplateView):
    template_name = 'home.html'

class FurCreateView(CreateView):
    model = Fur
    fields = {'name', 'sort', 'farm', 'price'}
    template_name = 'fur_create.html'
    success_url = '/furform'

class FarmCreateView(CreateView):
    model = Farm
    fields = {'adress', 'surname', 'phone'}
    template_name = 'farm_create.html'
    success_url = '/farmform'



def FarmList(request):
    farms = Farm.objects.all()
    return render(request, 'farm_list.html', {'farms':farms})


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['fur']

class FurList(ListView):
    model = Fur
    template_name = 'fur_list.html'

def buy(request, pk):
    fur = get_object_or_404(Fur, fur_id=pk)
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user.id
            form.fur = fur
            form.save()
            return redirect("/home/")
    else:
        form = PurchaseForm()

    return render(request, "fur_buy.html", {"fur": fur, "form": form})

def addReview(request, pk):
    fur = get_object_or_404(Fur, fur_id=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.text = form.text
            form.user_id = request.user.id
            form.fur = fur
            form.save()
            return redirect("/home/")
    else:
        form = ReviewForm()
    return render(request, "review_form.html", {"fur": fur, "form": form})

def deletePurchase(request,pk):
    purchase = get_object_or_404(Purchase, purchase_id=pk)
    purchase.delete()
    return render(request, "purchase_delete.html", {"purchase": purchase})

def deleteReview(request,pk):
    review = get_object_or_404(Review, review_id=pk)
    review.delete()
    return render(request, "review_delete.html", {"review": review})

def PurchaseView(request):
    purchases = Purchase.object.all().filter(user_id=request.user.id)
    reviews = Review.object.all().filter(user_id=request.user.id)
    return render(request, "profile.html", {"purchases": purchases, "reviews":reviews})

def ReviewList(request,pk):
    reviews = Review.object.all().filter(fur_id = pk)
    return render(request, "reviews.html", {'reviews':reviews})
