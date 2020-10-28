from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    address = models.CharField(max_length=60)
    nationality = models.CharField(max_length=40)

class Auto(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField()

class Owner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    autos = models.ManyToManyField(Auto, through='Owns')
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    sex_vars=(
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=sex_vars)
    passport = models.IntegerField()

class Drive_docs(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.IntegerField()
    type = models.CharField(max_length=30)
    date_from = models.DateField()
    date_to = models.DateField()

class Owns(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()