from django.shortcuts import render
from django.http import Http404
#импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render #импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from belov.models import Car #импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)
def detail(request, car_id):
    try: #метод try-except - обработчик исключений
        p = Car.objects.get(pk=car_id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Car.DoesNotExist:
        raise Http404("Poll does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'details.html', {'Car': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"
# Create your views here.
