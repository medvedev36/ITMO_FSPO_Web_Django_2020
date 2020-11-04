from django.db import models
from django.utils import timezone


class Ship(models.Model):
    ship_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    release = models.DateField()
    deadline = models.DateField()
    team = models.IntegerField()
    economy_price = models.DecimalField(max_digits=10, decimal_places=2)
    business_price = models.DecimalField(max_digits=10, decimal_places=2)
    luxury_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Route(models.Model):
    route_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    days = models.IntegerField()
    stops = models.IntegerField()

    def __str__(self):
        return self.name


class Excursion(models.Model):
    excursion_id = models.IntegerField(primary_key=True, unique=True)
    e_ship_id = models.ForeignKey(Ship, blank=False, null=False, on_delete=models.CASCADE)
    e_route_id = models.ForeignKey(Route, blank=False, null=False, on_delete=models.CASCADE)
    departure = models.DateTimeField(default=timezone.now)
    economy_pass = models.IntegerField()
    business_pass = models.IntegerField()
    luxurious_pass = models.IntegerField()

    def __str__(self):
        return self.excursion_id

# Create your models here.
