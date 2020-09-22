from django.db import models


class Auto(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    state_number = models.CharField(max_length=9)


class Owner(models.Model):
    firstName = models.CharField(max_length=30)
    secondName = models.CharField(max_length=30)
    birthday = models.DateField()
    autos = models.ManyToManyField(Auto, through='Owning')


class Owning(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    dateBuy = models.DateField()
    dateSell = models.DateField()


class DriveLic(models.Model):
    number = models.IntegerField()
    TYPE_CHOICE = (
        ('R', 'Russia'),
        ('I', 'International')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICE)
    dateIssued = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)