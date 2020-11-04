from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    price = models.DecimalField(max_digits=10, max_length=10, decimal_places=2)


class AppUser(AbstractUser):
    USER_TYPES = [
        ('U', 'User'),
        ('O', 'Car owner'),
        ('R', 'Repairer')
    ]
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    cars = models.ManyToManyField(Car)


class InTripModel(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    begin = models.DateTimeField(auto_now=True)


class Repairs(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    repairer = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("I", "Input"),
        ("W", "Wage"),
        ("P", "Pay")
    ]
    user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    delta = models.DecimalField(max_digits=10, max_length=10, decimal_places=2)
    time = models.DateTimeField(auto_now=True)


class Trip(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    time = models.DecimalField(max_length=10, max_digits=10,default=0, decimal_places=0)
    transaction = models.ForeignKey(Transaction, on_delete=models.DO_NOTHING)
