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

    owner = models.ManyToManyField(CarOwner, through='Ownership')


class DriversLicense(models.Model):
    licenseNumber = models.IntegerField(primary_key=True)
    issueDate = models.DateField()
    type = models.CharField(max_length=8)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)


# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title