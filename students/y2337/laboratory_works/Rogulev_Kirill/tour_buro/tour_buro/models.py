from django.db import models

from django.contrib.auth.models import User

class Bus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("name", max_length=45)
    mileage = models.IntegerField(null=True)

class Excursion_route(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("name", max_length=45)
    start_location = models.CharField("start_location", max_length=45)
    end_location = models.CharField("end_location", max_length=45)
    length = models.IntegerField()

class Crew_member(models.Model):
    id = models.IntegerField(primary_key=True)
    second_name = models.CharField("second_name", max_length=45)
    exp = models.IntegerField()
    category = models.IntegerField()
    adress = models.CharField("adress",max_length=45)
    birth_year = models.IntegerField()
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)

class Completed_trip(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    n_passengers = models.IntegerField()
    price = models.IntegerField()
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Excursion_route, on_delete=models.CASCADE)
