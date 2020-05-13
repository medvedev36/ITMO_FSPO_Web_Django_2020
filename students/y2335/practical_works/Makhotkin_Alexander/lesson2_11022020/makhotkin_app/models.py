from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class Car(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    state_number = models.CharField(max_length=9)


class OwnerExtension(AbstractUser):
    passport = models.CharField(max_length=6)
    home_address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)


class Owner(models.Model):
    owner_extension = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    born = models.DateField()
    cars = models.ManyToManyField(Car, through='Have_car')


class Have_car(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_buy = models.DateField()
    date_sale = models.DateField()


class DriverLicense(models.Model):
    number = models.CharField(max_length=10)
    date_issued = models.DateField()
    LICENSE_TYPE_CHOISE = [
        ('S', 'Standart'),
        ('I', 'International'),
    ]
    type = models.CharField(choices=LICENSE_TYPE_CHOISE, max_length=1)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
