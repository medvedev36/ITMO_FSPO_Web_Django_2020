from django.db import models


class Auto(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gov_number = models.CharField(max_length=30)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateField()


class Ownership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    data_start = models.DateField()
    data_end = models.DateField()


TYPE = (('M', 'Minivan'),
        ('S', 'Super car'),
        ('R', 'Roadster'),
        ('L', 'Limousine'))


class DriverDoc(models.Model):
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=5, choices=TYPE)
    date = models.DateField()
    driver = models.ForeignKey(Person, on_delete=models.CASCADE)


