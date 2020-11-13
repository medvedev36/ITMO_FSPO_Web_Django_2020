import datetime

from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField(("Date"), default=datetime.date.today)


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


class Possession(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField(("Date"), default=datetime.date.today)
    final_date = models.DateField(("Date"), default=datetime.date.today)
