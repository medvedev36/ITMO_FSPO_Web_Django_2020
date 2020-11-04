from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404

from .models import *
from .forms import *

# Create your views here.
def home(request):    
    context = {
        'categories': Category.objects.all()[:10],
        'brands': Brand.objects.all()[:10],
        'products': Product.objects.all().order_by('name')[:20],
    }
    return render(request, 'online/home.html', context)

def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('.')
    else:
        form = UserLoginForm()
    context = {
        'form': form, 
        'confirm': 'Войти',
        'categories': Category.objects.all()[:10],
        'brands': Brand.objects.all()[:10],
    }
    return render(request, 'online/form.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        'purchases': Purchase.objects.filter(customer=request.user).order_by('-date'),
        'categories': Category.objects.all()[:10],
        'brands': Brand.objects.all()[:10],
        'form': UserUpdateForm(instance=request.user)
    }
    return render(request, 'online/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'online/form.html', {'form': form, 'confirm': 'Зарегистрировать'})

def my_logout(request):
    logout(request)
    return redirect('home')

@login_required
def buy_product(request, instock):
    instock = get_object_or_404(InStock, id=instock)
    if instock.quantity == 0:
        return HttpResponseNotFound()
    if request.method == 'POST':
        Purchase.objects.create(customer=request.user, instock=instock)
        instock.quantity -= 1
        instock.save()
        return redirect('profile')
    return render(request, 'online/purchase_confirm.html', {'object': instock})


class CategoryListView(ListView):
    model = Category
    template_name = 'online/category_all.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()[:10]
        context['brands'] = Brand.objects.all()[:10]
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'online/category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()[:10]
        context['brands'] = Brand.objects.all()[:10]
        context['object_list'] = Product.objects.filter(category=context['object'])
        return context


class BrandListView(ListView):
    model = Brand
    template_name = 'online/brand_all.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()[:10]
        context['brands'] = Brand.objects.all()[:10]
        return context


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'online/form.html'
    fields = ['name', 'phone', 'website']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()[:10]
        context['brands'] = Brand.objects.all()[:10]
        context['confirm'] = 'Добавить бренд'
        return context


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'online/brand_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()[:10]
        context['brands'] = Brand.objects.all()[:10]
        context['object_list'] = Product.objects.filter(brand=context['object'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'online/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()[:10]
        context['brands'] = Brand.objects.all()[:10]
        context['available'] = InStock.objects.filter(product=context['object'])
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'online/form.html'
    fields = ['name', 'brand', 'category']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()[:10]
        context['brands'] = Brand.objects.all()[:10]
        context['confirm'] = 'Добавить товар'
        return context


class StoreDetailView(DetailView):
    model = Store
    template_name = 'online/store_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()[:10]
        context['brands'] = Brand.objects.all()[:10]
        return context
