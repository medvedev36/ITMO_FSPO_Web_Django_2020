from django.db import models
from django.utils import timezone

# Create your models here.

class Boat(models.Model):
    boat_number = models.IntegerField(primary_key=True, unique=True)
    mark = models.CharField(max_length=40)

class Officer(models.Model):
    badge = models.IntegerField(primary_key=True, unique=True)
    surname = models.CharField(max_length=40)
    post = models.CharField(max_length=40)
    enrollment = models.DateTimeField(default=timezone.now())
    experience = models.IntegerField()
    birthday = models.DateField()
    boat_number = models.ForeignKey(Boat, blank=False, null=False, on_delete=models.CASCADE)


class Patrol(models.Model):
    patrol_id = models.IntegerField(primary_key=True, unique=True)
    boat_number = models.ForeignKey(Boat, blank=False, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())
    district = models.IntegerField()
    intruders = models.IntegerField()
    reward = models.IntegerField()

