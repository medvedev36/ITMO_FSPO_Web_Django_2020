from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    passport = models.IntegerField(unique=True, null=True)
    address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=100, null=True)


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)


class Owner(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    cars = models.ManyToManyField(Car, through='Ownership')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class Drivers_license(models.Model):
    LIST_OF_TYPES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    number = models.CharField(max_length=50)
    start_date = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=LIST_OF_TYPES)


class Ownership(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

