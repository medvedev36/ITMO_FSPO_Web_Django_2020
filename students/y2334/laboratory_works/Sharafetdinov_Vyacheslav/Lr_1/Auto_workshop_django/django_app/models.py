from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):  # Расширенная модель пользователя
    patronymic = models.CharField(max_length=50, blank='True', verbose_name='Отчество')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона')


class Workshop(models.Model):  # Мастерская
    number = models.IntegerField(unique=True, verbose_name='Номер')
    address = models.CharField(max_length=50, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Мастерская'
        verbose_name_plural = 'Мастерские'


class Served_brands(models.Model):  # Обслуживаемые в мастерской марки
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='brands', verbose_name='Мастерская')
    brand = models.CharField(max_length=30, db_index=True, verbose_name='Обслуживаемая марка')

    class Meta:
        verbose_name = 'Обслуживаемая марка'
        verbose_name_plural = 'Обслуживаемые марки'


class Auto(models.Model):  # Автомобиль
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='autos',
                              verbose_name='Владелец')
    number = models.CharField(max_length=15, verbose_name='Гос. номер')
    brand = models.CharField(max_length=30, verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    year = models.IntegerField(verbose_name='Год выпуска')
    tech_passport = models.CharField(max_length=20, unique=True, verbose_name='Тех. паспорт')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Employee(models.Model):  # Работник автомастерской
    workshop = models.ForeignKey(Workshop, on_delete=models.SET_NULL, null=True, verbose_name='Мастерская')
    autos = models.ManyToManyField(Auto, through='Work', related_name='employees', verbose_name='Ремонтные работы')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Work(models.Model):  # Ремонтные работы, проводимые работником
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='employee_works',
                                 verbose_name='Работник')
    auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True, related_name='auto_works',
                             verbose_name='Автомобиль')
    date_beg = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(blank=True, verbose_name='Дата завершения')
    description = models.TextField(verbose_name='Описание работ')
    price = models.FloatField(blank=True, verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Ремонтная работа'
        verbose_name_plural = 'Ремонтные работы'


class Application(models.Model):  # Заявка на ремонт
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='applications_auto', verbose_name='Автомобиль')
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='applications_workshop',
                                 verbose_name='Мастерская')
    date = models.DateField(verbose_name='Дата записи')
    status_vars = (
        ('cons', 'В рассмотрении'),
        ('conf', 'Подтверждено'),
        ('refs', 'Отклонено'),
    )
    status = models.CharField(max_length=4, choices=status_vars)
    date_init = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Заявка на ремонт'
        verbose_name_plural = 'Заявки на ремонт'
