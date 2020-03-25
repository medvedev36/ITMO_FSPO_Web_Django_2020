from django.db import models


class User (models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pass_num = models.IntegerField(max_length=10,primary_key=True)
    sex = models.CharField(max_length=1, choices=GENDERS)


class Auto (models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    prod_year = models.DateField()
    many_to_many_field = models.ManyToManyField(User, through='AutoUser')


class AutoUser(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_in = models.DateField()
    date_out = models.DateField()


class DriverLicence(models.Model):
    license_num = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(max_length=10)
    type = models.CharField(max_length=20)
    date = models.DateField()
