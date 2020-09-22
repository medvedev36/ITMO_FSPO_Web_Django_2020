from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Auto(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    state_number = models.CharField(max_length=9)


class userOwner(AbstractUser):
    passport = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)


class Owner(models.Model):
    userOwn = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    firstName = models.CharField(max_length=30)
    secondName = models.CharField(max_length=30)
    birthday = models.DateField()
    autos = models.ManyToManyField(Auto, through='Owning')


class Owning(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    dateBuy = models.DateField()
    dateSell = models.DateField()


class DriveLic(models.Model):
    number = models.IntegerField()
    TYPE_CHOICE = (
        ('R', 'Russia'),
        ('I', 'International')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICE)
    dateIssued = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)