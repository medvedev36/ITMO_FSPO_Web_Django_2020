from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


# Create your models here.
class User(AbstractUser):
    passport = models.IntegerField(unique=True, null=True)
    address = models.CharField(max_length=70, null=True)
    nationality = models.CharField(max_length=48, null=True)


class Car(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    model = models.CharField(max_length=30)
    provider = models.CharField(max_length=30)


class Owner(models.Model):
    SEXES = [('M', "Male"), ('F', "Female")]

    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=SEXES)
    car = models.ManyToManyField(Car, through='OwnerShip')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class CarLicense(models.Model):
    TYPES = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
    # id = models.IntegerField()
    type = models.CharField(max_length=1, choices=TYPES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class OwnerShip(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start = models.DateField()
    finish = models.DateField()
