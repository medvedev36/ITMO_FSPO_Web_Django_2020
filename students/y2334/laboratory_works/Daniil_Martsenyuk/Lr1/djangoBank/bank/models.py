from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Account(models.Model):
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, null=True)
    amount = models.FloatField(verbose_name='Сумма')

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'


class Client(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE, blank=True, null=True)
    account = models.ManyToManyField(Account, blank=True)
    name = models.CharField(verbose_name='Имя', max_length=30, blank=True, null=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=30, blank=True, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=50, blank=True, null=True)
    passport_number = models.CharField(verbose_name='Номер паспорта', max_length=20, unique=True, blank=True, null=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, unique=True, blank=True, null=True)
    age = models.CharField(max_length=10, verbose_name='Дата рождения', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    contract_code = models.ManyToManyField("Contract", blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Client.objects.create(user=instance)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Currency(models.Model):
    name_choice = (
        ('Ruble', 'Ruble'),
        ('Belarusian ruble', 'Belarusian ruble'),
        ('Euro', 'Euro'),
        ('Dollar', 'Dollar'),
        ('Hryvnia', 'Hryvnia')  # хуйня
    )
    name = models.CharField(max_length=30, choices=name_choice)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class Deposit(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    percent = models.FloatField(verbose_name='Процент в месяц')
    currency_code = models.ForeignKey('Currency', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вклад'
        verbose_name_plural = 'Вклады'


class Contract(models.Model):
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE, blank=True, null=True)
    deposit_code = models.ForeignKey('Deposit', on_delete=models.CASCADE, blank=True, null=True)
    deposit_date = models.DateField(verbose_name='Дата вклада', auto_now_add=True)
    depositAmount = models.FloatField(verbose_name='Сумма вклада')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'


class Employee(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)
    surname = models.CharField(verbose_name='Фамилия', max_length=30)
    age = models.IntegerField(verbose_name='Возраст')
    address = models.CharField(verbose_name='Адрес', max_length=50)
    passportID = models.CharField(verbose_name='Номер паспорта', max_length=20, unique=True)
    phoneNumber = models.CharField(verbose_name='Номер телефона', max_length=20, unique=True)
    profession_choice = (
        ('Administrator', 'Administrator'),
        ('Operator', 'Operator'),
        ('Director', 'Director'),
        ('Support', 'Support')
    )
    profession = models.CharField(verbose_name='Должность', max_length=30, choices=profession_choice)
    salary = models.IntegerField(verbose_name='Заработная плата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Support(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    report = models.TextField(max_length=540)

