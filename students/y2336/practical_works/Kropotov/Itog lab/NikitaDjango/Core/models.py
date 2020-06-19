from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import *

# Create your models here.
class Client(AbstractUser):
    balance = models.IntegerField(default=0)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    img = models.ImageField(default="default.jpg", upload_to='')

    def __str__(self):
        return self.username


class Fuel(models.Model):
    name = models.CharField(max_length=100)
    fuel_type = models.IntegerField(choices=FUEL_TYPE_CHOICES)
    metric = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FuelProvider(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class FuelStation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    provider = models.ForeignKey(FuelProvider, on_delete=models.CASCADE)
    fuels = models.ManyToManyField(Fuel, through='FuelInStation')

    def __str__(self):
        return self.name
        

class FuelInStation(models.Model):
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    price = models.FloatField()
    clients = models.ManyToManyField(Client, through='Purchase')

    def __str__(self):
        return '{} {}'.format(self.station, self.fuel)

class Purchase(models.Model):
    date = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fuel_in_station = models.ForeignKey(FuelInStation, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.client, self.amount)