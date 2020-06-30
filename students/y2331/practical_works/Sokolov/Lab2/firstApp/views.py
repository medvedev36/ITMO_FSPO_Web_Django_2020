from django.http import Http404
from django.shortcuts import render
from firstApp.models import CarOwner
from firstApp.models import Car
from firstApp.models import Ownership
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import GeeksModel


def detail(request, CarOwner_id):
    try:  # метод try-except - обработчик исключений
        p = CarOwner.objects.get(pk=CarOwner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'CarOwner.html', {'owner': p})


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = CarOwner.objects.all()

    return render(request, "listView.html", context)


class GeeksList(ListView):
    # specify the model for list view
    model = Car


from django.shortcuts import render

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm  # импортируем только-что созданную форму


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = GeeksForm(
        request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():  # Проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class GeeksCreate(CreateView):
    # specify the model for create view
    model = Car
    #     #
    #     #
    #     # # specify the fields to be displayed
    #     #
    fields = ['carMark', 'model','color','carNumber']

    # specify the model for create view
    # model = GeeksModel

    # specify the fields to be displayed

    # fields = ['title', 'description']
    success_url = '/ex4/'  # reverse_lazy('contact') или reverse

    def get_absolute_url(self): return '/ex4/'
