from django.db import models


class Disk(models.Model):
    sing = models.CharField(max_length=50)
    production_date = models.DateField()
    price = models.IntegerField()
    producer = models.CharField(max_length=50)


class Sing(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)
    date = models.DateField()
    type = models.CharField(max_length=50)


class Buy(models.Model):
    disk = models.CharField(max_length=50)


class Singer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
# Create your models here.
