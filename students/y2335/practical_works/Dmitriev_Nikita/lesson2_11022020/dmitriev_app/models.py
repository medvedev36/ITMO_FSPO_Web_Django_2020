from django.db import models


class Car(models.Model):
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    state_number = models.CharField(max_length=9)
    color = models.CharField(max_length=20)


class Owner(models.Model):
    firstName = models.CharField(max_length=20)
    secondName = models.CharField(max_length=30)
    birthday = models.DateField()
    cars = models.ManyToManyField(Car, through='Have')


class DriverLic(models.Model):
    num = models.IntegerField
    dateIssued = models.DateField
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    type = models.CharField(max_length=1, choices=TYPE)
    driver = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Have(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()
