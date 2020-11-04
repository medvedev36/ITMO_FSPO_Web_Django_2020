from django.db import models

# Create your models here.
from django.db import models


class Car(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=9)


class User(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    passport = models.IntegerField
    gender = models.CharField(max_length=3, choices=GENDER)

    users = models.ManyToManyField(Car, through='Ownership')


class Ownership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class License(models.Model):
    TYPE = (
        ('A', 'A'),
        ('A1', 'A1'),
        ('B', 'B'),
        ('B1', 'B1'),
        ('C', 'C'),
        ('C1', 'C1'),
        ('D', 'D'),
        ('D1', 'D1')
    )
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.IntegerField
    type = models.CharField(max_length=3, choices=TYPE)
    date_issued = models.DateField()



