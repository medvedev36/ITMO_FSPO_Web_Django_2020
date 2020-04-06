from django.db import models

# Create your models here.


class Car (models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField


class User (models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    passport = models.IntegerField
    gender = models.CharField(max_length=1, choices=GENDER)
    users = models.ManyToManyField(Car, through='Ownership')


class License (models.Model):
    TYPE = (
        ('H', 'Home'),
        ('F', 'Foreign'),
    )
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.IntegerField
    type = models.CharField(max_length=1, choices=TYPE)
    date_issued = models.DateField
    date_expired = models.DateField


class Ownership(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    cars = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
