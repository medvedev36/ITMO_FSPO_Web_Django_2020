from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=512)
    nationality = models.CharField(max_length=50)
    passport = models.CharField(max_length=10)


class Car(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=9)


class Owner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birthday = models.DateField
    cars = models.ManyToManyField(Car, through='Ownership')


class License(models.Model):
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    driver = models.ForeignKey(Owner, on_delete=models.CASCADE)
    num = models.IntegerField
    type = models.CharField(max_length=1, choices=TYPE)
    date_issued = models.DateField


class Ownership(models.Model):
    user = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
