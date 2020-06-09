from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class OwnerExt(AbstractUser):
    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    passport = models.CharField(max_length=10)

class Car(models.Model):
    year = models.IntegerField()
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    def __str__(self):
        return self.model
class Owner(models.Model):
    extended = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    gender_vars = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non-Gender')
    )
    sex = models.CharField(max_length=1, choices=gender_vars)
    cars = models.ManyToManyField(Car, through='Ownership')
    birthday = models.DateField()

class License(models.Model):
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    num = models.IntegerField
    driver = models.ForeignKey(Owner, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPE)
    dateIssued = models.DateField

class Ownership(models.Model):
    user3 = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()