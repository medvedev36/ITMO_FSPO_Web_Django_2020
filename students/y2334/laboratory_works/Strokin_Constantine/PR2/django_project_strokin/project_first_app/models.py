import datetime

from django.db import models
from django.http import HttpResponseNotFound, request
from django.shortcuts import render


class Owner(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.first_name


class License(models.Model):
    TYPE = (
        ('A', 'motorcycle'),
        ('B', 'car'),
        ('C', 'truck'),
        ('D', 'bus'),
    )
    number = models.IntegerField
    issue_date = models.DateField(("Date"), default=datetime.date.today)
    type = models.CharField(max_length=1, choices=TYPE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Car(models.Model):
    mark = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    number = models.CharField(max_length=32)
    owners = models.ManyToManyField(Owner, through='Possession')

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return ""

class Possession(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField(("Date"), default=datetime.date.today)
    final_date = models.DateField(("Date"), default=datetime.date.today)
