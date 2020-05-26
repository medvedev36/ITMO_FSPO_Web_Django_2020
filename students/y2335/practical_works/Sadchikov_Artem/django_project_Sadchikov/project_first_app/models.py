from django.db import models

class Car(models.Model):
    number = models.CharField(max_length = 10)
    model = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)
    governmentNumber = models.IntegerField()

class Car_owner(models.Model):
    cars = models.ManyToManyField(Car, through = 'Possession')
    firstName = models.CharField(max_length = 50)
    secondName = models.CharField(max_length = 50)
    birthday = models.DateField()

class Driver_license(models.Model):
    number = models.IntegerField()
    dateIssued = models.DateField()
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    type = models.CharField(max_length = 1, choices=TYPE)
    driver = models.ForeignKey(Car_owner, on_delete = models.CASCADE)

class Possession(models.Model):
    user = models.ForeignKey(Car_owner, on_delete = models.CASCADE)
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()
