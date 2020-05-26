from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import Owner, Car
from django.views.generic.list import ListView
from django.shortcuts import render
from .forms import OwnerForm
from django.views.generic.edit import CreateView

def details(request, owner_id):
    try:
        owner = Owner.objects.get(pk = owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owners/details.html', {'owner': owner})

def listOwners(request):
    owners = Owner.objects.all()
    return render(request, 'owners/list.html', {'owners': owners})

def ownerView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OwnerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OwnerForm()

    return render(request, 'ownerview.html', {'form': form})

class CarList(ListView):
    model = Car
    template_name = "carlist.html"
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

# Create your views here.
