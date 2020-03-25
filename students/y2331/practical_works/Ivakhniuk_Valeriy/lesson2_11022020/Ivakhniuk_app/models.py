from django.db import models


class DriverLicense(models.Model):
    number = models.IntegerField(max_length=15)
    type = (
        'Foreign',
        'Homeland',
    )
    date_getting = models.DateField()


class User(models.Model):
    drive_license_id = models.ForeignKey(DriverLicense, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender_ch = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Undefined'),
    ])
    passport_id = models.IntegerField(max_length=10)


class Auto(models.Model):
    #driving = models.ManyToManyField(User, through="Usage")
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_year = models.DateField()


class Usage(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    sell_date = models.DateField()
    buy_date = models.DateField()
