from django.http import Http404
from django.shortcuts import render
from dmitriev_app.models import Owner, Car
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import OwnerForm


def detail(request, owner_id):
    try:  # метод try-except - обработчик исключений
        owner = Owner.objects.get(
            pk=owner_id)  # переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Owner.DoesNotExist:
        raise Http404(
            "Owner does not exist")  # исключение которое будет вызвано, если блок try вернет значения False (не будут найдены записи в таблице Poll
    return render(request, 'owner.html', {
        'owner': owner})  # данная строка рендерит хтмл страницу detail.html и передает в него объект p, который в хтмл шаблоне будет называться poll


def list_owners(request):
    context = {}
    context["dataset"] = Owner.objects.all()
    return render(request, 'list_owners.html', context)


class CarList(ListView):
    template_name = "list_cars.html"
    model = Car


def create_owners(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owners.html", context)


class CarsCreate(CreateView):
    template_name = "create_cars.html"
    success_url = "."
    model = Car
    fields = ['mark', 'model', 'state_number', 'color']

