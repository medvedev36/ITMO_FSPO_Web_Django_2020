from django.db import models

# Create your models here.


class DriverLicense(models.Model):
    TypeChoice = (
        ('A', 'Motorcycle'),
        ('B', 'Easyweight'),
        ('C', 'Heavyweight'),
        ('D', 'Bus'),
        ('M', 'Quadrocycles'),
    )
    IdPerson = models.ForeignKey('Person', on_delete=models.CASCADE)
    Number = models.IntegerField()
    DateOfCreate = models.DateField()
    Type = models.CharField(max_length=15, choices=TypeChoice)


class Car(models.Model):
    LogoChoice = (
        ('BMW', 'Bayerische Motoren Werke AG'),
        ('Volvo', 'Volvo'),
        ('Peugot', 'Peugot'),
        ('VAZ', 'Russian Automobile')
    )

    ColorChoice = (
        ('White', 'White'),
        ('Black', 'Black'),
        ('Red', 'Red'),
        ('Pink', 'Pink'),
        ('Orange', 'Orange'),
        ('Blue', 'Blue')
    )

    id = models.AutoField(primary_key=True)
    Logo = models.CharField(max_length=10, choices=LogoChoice)
    Model = models.CharField(max_length=25)
    Color = models.CharField(max_length=10, choices=ColorChoice)
    Number = models.CharField(max_length=6)


class Person(models.Model):
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Birthday = models.DateField()
    id = models.AutoField(primary_key=True)
    cars = models.ManyToManyField(Car, through='Owner')

    def __str__(self):
        return self.Name


class Owner(models.Model):
    Name = models.ForeignKey(Person, on_delete=models.CASCADE)
    CarInfo = models.ForeignKey(Car, on_delete=models.CASCADE)
    StartDate = models.DateField()
    EndDate = models.DateField()
