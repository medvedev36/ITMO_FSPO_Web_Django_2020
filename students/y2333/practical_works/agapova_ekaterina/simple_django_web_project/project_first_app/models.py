from django.db import models


class Car(models.Model):

    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    carNumber = models.CharField(max_length=10)
    color = models.CharField(max_length=50)


class Owner(models.Model):

    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    car = models.ManyToManyField(Car, through='Possession')


class Possession(models.Model):

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()


class License(models.Model):

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.IntegerField
    types = (
        ('A', 'Мотоцикл'),
        ('B', 'Легковой автомобиль'),
        ('C', 'Грузовой автомобиль'),
        ('D', 'Автобус')
    )
    type = models.CharField(max_length=1, choices=types)
    dateIssued = models.DateField
