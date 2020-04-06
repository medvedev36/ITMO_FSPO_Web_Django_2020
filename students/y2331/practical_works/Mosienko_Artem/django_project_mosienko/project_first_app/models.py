from django.db import models
from django.core.validators import MinLengthValidator

DRIVER_LICENSE_TYPE_CHOICES = (
    ('A', 'Any type of motorbike'),
    ('B', 'Motorised vehicle under 3.5 tons (optionally with light trailer)'),
    ('C', 'Motorised vehicle over 3.5 tons (optionally with light trailer, up to 750 kg)'),
    ('D', 'Bus (has more than 8 passenger seats) (optionally with light trailer, up to 750 kg)'),
    ('BE', 'Motorised vehicle under 3.5 tons with heavy trailer'),
    ('CE', 'Motorised vehicle over 3.5 tons with heavy trailer'),
    ('DE', 'Bus with heavy trailer'),
    ('M', 'Moped, assigned automatically if you have any other category open'),
    ('Tram', 'Tram'),
    ('Trolleybus', 'Trolleybus'),
)


class Car (models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    registration_plate = models.CharField(max_length=7, validators=[MinLengthValidator(7)])


class Owner (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    cars = models.ManyToManyField(Car, through='Ownership')


class Ownership (models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class License (models.Model):
    license_number = models.CharField(max_length=10, validators=[MinLengthValidator(7)])
    date_of_issue = models.DateField()
    type = models.CharField(
        max_length=10,
        choices=DRIVER_LICENSE_TYPE_CHOICES
    )
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
