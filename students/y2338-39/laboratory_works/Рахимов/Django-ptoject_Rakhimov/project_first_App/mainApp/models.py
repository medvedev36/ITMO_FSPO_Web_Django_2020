from django.db import models

TypesForNomer = (
    ('s', 'Standart'),
    ('p', 'President'),
    ('e', 'Econom'),
    ('l', 'Lux'),
)

TypesForStatus = (
    ('b', 'Busy'),
    ('f', 'Free'),
    ('z', 'Booked'),
)


class City(models.Model):
    name_city = models.CharField(max_length=30)
    name_country = models.CharField(max_length=30)

    def __str__(self):
        return self.name_city


class Hotel(models.Model):
    address = models.CharField(max_length=30)
    name_hotel = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class InfoAboutNomer(models.Model):
    price = models.IntegerField()
    count_customers = models.IntegerField()
    type_nomer = models.CharField(max_length=1, choices=TypesForNomer)


class Nomer(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    numberOfNomer = models.IntegerField()
    info = models.ForeignKey(InfoAboutNomer, on_delete=models.CASCADE)


class Customers(models.Model):
    fio = models.CharField(max_length = 30)
    number_passport_customer = models.BigIntegerField()
    number_phone_cus = models.BigIntegerField()
    nomer = models.ManyToManyField(Nomer, through='Registration')


class Registration(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    nomer = models.ForeignKey(Nomer, on_delete=models.CASCADE)
    date_entry = models.DateField()
    date_exit = models.DateField()
    status_nomer = models.CharField(max_length=1, choices=TypesForStatus)


class currentCusromer(models.Model):
    fio = models.CharField(max_length=30)
    passport = models.BigIntegerField()
    phone = models.BigIntegerField()
# Create your models here.
