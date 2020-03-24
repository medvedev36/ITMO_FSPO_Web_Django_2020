from django.db import models


# Create your models here.
class Car(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=9)


class Owner(models.Model):
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
