from django.db import models


class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_date = models.DateField()


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    passport_id = models.IntegerField()
    owners_car = models.ManyToManyField(Car, through='Document')


class Document(models.Model):
    person = models.ForeignKey(Owner, on_delete=models.CASCADE)
    machine = models.ForeignKey(Car, on_delete=models.CASCADE)
    registration_date = models.DateField()
    drop_date = models.DateField()


class DriverLicense(models.Model):
    License_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    LICENSE_CHOICE = (
        ('G', 'Global'),
        ('L', 'Local'),
    )
    license_type = models.CharField(max_length=1, choices=LICENSE_CHOICE)
    license_date = models.DateField()