from django.urls import path
from . import views #подключение файла контроллеров,описанного в пункте 3
urlpatterns = [
    path('owner/<int:CarOwner_id>/', views.detail), #пример вызова контроллера (функции) с именем "special_case_200" из файда views
    # path('articles/<int:year>/', views.year_archive), #пример вызова контроллера (функции) с именем "year_archive" из файда viewsи передачи в него переменной "year"
]