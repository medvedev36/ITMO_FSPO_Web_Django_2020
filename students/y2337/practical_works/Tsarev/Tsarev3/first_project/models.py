from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    passport = models.IntegerField(unique=True, null=True)
    address = models.CharField(max_length=150, null=True)
    nationality = models.CharField(max_length=30, null=True)


class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    birthday = models.DateField()
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class Auto(models.Model):
    COLOR = (
        ('Black', 'Black'),
        ('Yellow', 'Yellow'),
        ('White', 'White'),
        ('Green', 'Green'),
        ('Blue', 'Blue')
    )
    auto_id = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=10, choices=COLOR)
    license_plate = models.CharField(max_length=6)
    model = models.CharField(max_length=30)
    own = models.ManyToManyField(Owner, through='Possession')

    def get_absolute_url(self):
        return f'/auto/{self.auto_id}'


class Certification(models.Model):
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('M', 'M'),
    )
    id_cert = models.IntegerField(primary_key=True)
    release_date = models.DateField()
    type = models.CharField(max_length=2, choices=TYPE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Possession(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    date_rec = models.DateField()
    date_end = models.DateField()
