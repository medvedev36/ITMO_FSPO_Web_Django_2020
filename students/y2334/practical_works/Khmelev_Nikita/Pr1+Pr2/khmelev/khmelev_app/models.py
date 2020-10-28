from django.db import models

class Car(models.Model):
    year = models.IntegerField()
    mark = models.CharField(max_length = 30)
    model = models.CharField(max_length = 30)

    def __str__(self):
        return self.model


class Owner(models.Model):
    firstName = models.CharField(max_length = 50)
    secondName = models.CharField(max_length = 50)
    gender_vars = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non-Gender')
    )
    sex = models.CharField(max_length=1, choices=gender_vars)
    cars = models.ManyToManyField(Car, through = 'Ownership')
    passport = models.CharField(max_length=10)

    def __str__(self):
        return self.secondName

class License(models.Model):
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    num = models.IntegerField()
    driver = models.ForeignKey(Owner, on_delete = models.CASCADE)
    type = models.CharField(max_length = 1, choices=TYPE)
    dateIssued = models.DateField()

    def __str__(self):
        return '{} {}'.format(self.num, self.driver)

class Ownership(models.Model):
    user = models.ForeignKey(Owner, on_delete = models.CASCADE)
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()

    def __str__(self):
        return '{} {} {}'.format(self.dateEnd - self.dateStart, self.car, self.user)