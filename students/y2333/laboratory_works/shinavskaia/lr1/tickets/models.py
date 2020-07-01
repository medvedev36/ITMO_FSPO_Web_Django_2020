from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


from .choices import USER_TYPE_CHOICE, PAYMENT_TYPE_CHOICE


# Create your models here.
class BusType(models.Model):
    name = models.CharField(max_length=30)
    people_capacity = models.PositiveIntegerField()
    engine_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Driver(models.Model):
    image = models.ImageField(upload_to='pic_drivers', default='driver_default.jpg')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    passport_number = models.PositiveIntegerField()
    phone = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    birth = models.DateField(default='1980-05-24')
    hiring_date = models.DateField(default='2020-01-12')
    rides = models.ManyToManyField('Bus', through='Ride')

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name()


class Bus(models.Model):
    number = models.CharField(max_length=30)
    bus_type = models.ForeignKey(BusType, on_delete=models.CASCADE)
    usage_start_date = models.DateField(auto_now_add=True)
    brand = models.CharField(max_length=30, default='MAN')

    def __str__(self):
        return '{} {}'.format(self.brand, self.number)


class Ride(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    where_from = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='where_from')
    where = models.ForeignKey(Station, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return 'From {} to {}'.format(self.where_from, self.where)


class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    payment_type = models.IntegerField(choices=PAYMENT_TYPE_CHOICE, default=1)
    rating = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user, self.ride)