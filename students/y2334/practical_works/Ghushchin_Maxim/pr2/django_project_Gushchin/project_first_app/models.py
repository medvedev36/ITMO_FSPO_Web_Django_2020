from django.db import models


class Auto(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gov_number = models.CharField(max_length=30)

    def __str__(self):
        return self.mark


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cars = models.ManyToManyField(Auto, through='Ownership')
    date = models.DateField()

    def __str__(self):
        return self.first_name


class Ownership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    data_start = models.DateField()
    data_end = models.DateField()


TYPE = (('SC', 'sport car'),
        ('С', 'crossover'),
        ('M', 'micro car'))


class DriverDoc(models.Model):
    number = models.CharField(max_length=10)
    date = models.DateField()
    type = models.CharField(max_length=30, choices=TYPE)
    driver = models.ForeignKey(Person, on_delete=models.CASCADE)


