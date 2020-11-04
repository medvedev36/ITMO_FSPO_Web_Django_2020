from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    passport = models.IntegerField(unique=True, null=True)
    address = models.CharField(max_length=128, null=True)
    nationality = models.CharField(max_length=48,  null=True)

class Car(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    brand = models.CharField("Марка", max_length=32)
    model = models.CharField("Модель", max_length=32)
    color = models.CharField("Цвет", max_length=32)
    num = models.CharField("Гос. номер", max_length=32)

    def get_absolute_url(self):
        return '/car/new'

class Owner(models.Model):
    first_name = models.CharField("Имя владельца", max_length=32)
    last_name = models.CharField("Фамилия владельца", max_length=48)
    birthday = models.DateField("Дата рождения владельца")
    cars = models.ManyToManyField(Car, through='Ownership')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

class License(models.Model):
    TYPES = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
    id = models.AutoField(primary_key=True)
    type = models.CharField("Тип удостоверения", max_length=1, choices=TYPES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    issue_date = models.DateField("Дата получение")
    expiration_date = models.DateField("Дата окончания", null=True)


class OwnerShip(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start = models.DateField("Начало владения")
    finish = models.DateField("Продажа")