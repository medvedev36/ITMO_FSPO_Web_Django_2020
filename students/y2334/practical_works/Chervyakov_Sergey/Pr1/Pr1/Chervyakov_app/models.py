from django.db import models


class Auto(models.Model):
    Brand = models.CharField(max_length=50)
    name = models.CharField(max_length=60)
    development_Year = models.CharField(max_length=4)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    passport = models.CharField(max_length=10)
    SEX_TYPES = [
        ('M', 'Male'),
        ('W', 'Female'),
        ('I', 'I dont wanna tell you')
    ]
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    obt = models.ManyToManyField(Auto, through='Obtaining')


class Obtaining(models.Model):
    First_date = models.DateField()
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Auto = models.ForeignKey(Auto, on_delete=models.CASCADE)


class Licence(models.Model):
    ForKey = models.ForeignKey(Person, on_delete=models.CASCADE)
    Number = models.CharField(max_length=8)
    PRIVALAGESSESES = (
        ('Rg','Regional'),
        ('WW', 'World')
    )
    privalages = models.CharField(max_length=9, choices=PRIVALAGESSESES)
    Date_of_obtaining = models.DateField()

