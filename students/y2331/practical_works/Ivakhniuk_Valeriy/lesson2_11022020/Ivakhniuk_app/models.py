from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


class User1(AbstractUser):
    home_adress = models.CharField(max_length=30, null=True ,blank=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)
    pasport = models.IntegerField(max_length=15, null = True, blank=True)


class DriverLicense(models.Model):
    number = models.IntegerField(max_length=15)
    type = (
        'Foreign',
        'Homeland',
    )
    date_getting = models.DateField()


class User(models.Model):
    drive_license_id = models.ForeignKey(DriverLicense, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender_ch = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Undefined'),
    ])
    newrow = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    passport_id = models.IntegerField(max_length=10)



class Auto(models.Model):
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_year = models.DateField()


class Usage(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    sell_date = models.DateField()
    buy_date = models.DateField()
