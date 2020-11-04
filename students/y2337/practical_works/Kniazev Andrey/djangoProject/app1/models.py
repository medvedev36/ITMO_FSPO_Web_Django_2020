from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


class User(AbstractUser):
    passport = models.IntegerField(unique=True, null=True, default=0)
    address = models.CharField(max_length=150, null=True, default="")
    nationality = models.CharField(max_length=30, null=True, default="")


class Owner(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    # User = get_user_model()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # info = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_valid(self):
        pass


class Car(models.Model):
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=30)


class Cert(models.Model):
    date = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Own(models.Model):
    beginDate = models.DateField()
    endDate = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
