from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Auto(models.Model):

    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.model} {self.brand} [{self.license_plate}]'


class Possession(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.owner.username} {self.auto}'
