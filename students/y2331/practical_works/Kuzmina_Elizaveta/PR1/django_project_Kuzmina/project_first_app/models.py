from django.db import models


# Create your models here.
class CarOwner(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthDate = models.DateField()


class Car(models.Model):
    carMark = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    carNumber = models.CharField(max_length=9)


class DriversLicense(models.Model):
    CATEGORY = (
        ('A', 'Motorcycle'),
        ('B', 'Auto'),
        ('C', 'Truck'),
        ('D', 'Bus'),
        ('M', 'Moped'),
    )
    licenseNumber = models.IntegerField(primary_key=True, max_length=30)
    issueDate = models.DateField()
    type = models.CharField(max_length=10, choices=CATEGORY)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
