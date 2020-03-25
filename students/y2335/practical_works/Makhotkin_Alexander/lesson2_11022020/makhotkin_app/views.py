from django.shortcuts import render
from django.http import Http404 #импортирует метод обработки ситуации, когда нет необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render
from makhotkin_app.models import Owner #импортирует таблицу Poll из модели данных, где polls - название приложения


def detail(request, owner_id):
    try: #метод try-except - обработчик исключений
        p = Owner.objects.get(pk=owner_id) #переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Owner.DoesNotExist:
        raise Http404("Auto-owner does not exist") #исключение которое будет вызвано, если блок try вернет значения False (не будут найдены записи в таблице Poll
    return render(request, 'owner.html', {'owner': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект p, который в хтмл шаблоне будет называться poll



# Create your views here.
