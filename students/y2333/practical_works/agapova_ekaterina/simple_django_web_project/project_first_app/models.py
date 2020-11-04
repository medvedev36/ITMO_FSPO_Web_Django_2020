from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    passport = models.CharField(max_length=10)
    homeAddress = models.CharField(max_length=256)
    nationality = models.CharField(max_length=20)


class Car(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    carNumber = models.CharField(max_length=10)
    color = models.CharField(max_length=50)


class Owner(models.Model):
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    car = models.ManyToManyField(Car, through='Possession')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Possession(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.IntegerField
    types = (
        ('A', 'Мотоцикл'),
        ('B', 'Легковой автомобиль'),
        ('C', 'Грузовой автомобиль'),
        ('D', 'Автобус')
    )
    type = models.CharField(max_length=1, choices=types)
    dateIssued = models.DateField
