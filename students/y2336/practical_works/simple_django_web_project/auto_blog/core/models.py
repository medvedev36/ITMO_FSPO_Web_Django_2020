from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Vehicle(models.Model):

    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.model} {self.brand} [{self.license_plate}]'


class Possession(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.owner.username} {self.auto}'
    

class License(models.Model):
    type_choices = [('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]
    number = models.CharField(max_length=10)
    date_of_issue = models.DateField()
    type_of_license = models.CharField(max_length=1, choices=type_choices)
    holder = models.ForeignKey(User, on_delete=models.CASCADE)
