from django.db import models

class Car(models.Model):
    number = models.CharField(max_length = 10)
    mark = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)


class Owner(models.Model):
    firstName = models.CharField(max_length = 50)
    secondName = models.CharField(max_length = 50)
    birthday = models.DateField
    cars = models.ManyToManyField(Car, through = 'Ownership')

class License(models.Model):
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    num = models.IntegerField
    driver = models.ForeignKey(Owner, on_delete = models.CASCADE)
    type = models.CharField(max_length = 1, choices=TYPE)
    dateIssued = models.DateField

class Ownership(models.Model):
    user = models.ForeignKey(Owner, on_delete = models.CASCADE)
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()
