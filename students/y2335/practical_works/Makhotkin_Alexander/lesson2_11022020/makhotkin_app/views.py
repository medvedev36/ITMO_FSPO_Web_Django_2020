from django.shortcuts import render
from django.http import Http404 #импортирует метод обработки ситуации, когда нет необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render
from makhotkin_app.models import Owner #импортирует таблицу Poll из модели данных, где polls - название приложения
from makhotkin_app.models import Car
from django.views.generic.list import ListView
from .forms import OwnerForm
from django.views.generic.edit import CreateView

def detail(request, owner_id):
    try: #метод try-except - обработчик исключений
        p = Owner.objects.get(pk=owner_id) #переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Owner.DoesNotExist:
        raise Http404("Auto-owner does not exist") #исключение которое будет вызвано, если блок try вернет значения False (не будут найдены записи в таблице Poll
    return render(request, 'owner.html', {'owner': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект p, который в хтмл шаблоне будет называться poll


def list_owners(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Owner.objects.all()

    return render(request, "list_owners.html", context)


class CarsList(ListView):
    template_name = "list_cars.html"
    model = Car


def owner_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():  # Проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "owner_form.html", context)


class CarCreate(CreateView):
    template_name = "car_form.html"
    success_url = "."

    # specify the model for create view
    model = Car

    # specify the fields to be displayed
    fields = ['mark', 'model', 'color', 'state_number']

# Create your views here.
