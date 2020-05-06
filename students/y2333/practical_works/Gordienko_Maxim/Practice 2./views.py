# Create your views here.
from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import Http404
from .models import User, Car
from .forms import UserForm
from django.views.generic.edit import CreateView


def details(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'owner.html', {'User': user})


def ListUsers(request):
    users = User.objects.all()
    return render(request, 'owners.html', {'Users': users})


def UserView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'ownerview.html', {'form': form})


class CarList(ListView):
    model = Car
    template_name = "car_list.html"
    context_object_name = "cars"

    def get_queryset(self):
        return Car.objects.all()


class CarCreate(CreateView):
    model = Car
    fields = ['mark', 'model']
    template_name = "carform.html"
    context_object_name = "cars"
    success_url = '/carform'

    def get_queryset(self):
        return Car.objects.all()