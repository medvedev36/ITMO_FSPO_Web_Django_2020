from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ClientUser(AbstractUser):
    image = models.ImageField(upload_to='pic_users')
    phone_number = models.CharField(max_length=20)
    passport_number = models.CharField(max_length=100)


class License(models.Model):
    type_choices = [('A', 'A'),
                    ('B', 'B'),
                    ('C', 'C')]
    user = models.OneToOneField('ClientUser', on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField(max_length=50)
    date_of_issue = models.DateField()
    type_of_license = models.CharField(max_length=1, choices=type_choices)


class CarClass(models.Model):
    name = models.CharField(max_length=20)
    rent_price = models.FloatField()
    min_car_price = models.IntegerField()
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class PickUpPoint(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address


class Car(models.Model):
    car_image = models.ImageField(upload_to='pic_cars')
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=20)
    sits_number = models.IntegerField(default=5)
    car_price = models.IntegerField()
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand + ' ' + self.model


class Rent(models.Model):
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    issue_datetime = models.DateTimeField()
    return_datetime = models.DateTimeField()
    actual_return_datetime = models.DateTimeField(null=True, blank=True)
    taken_from = models.ForeignKey(PickUpPoint, on_delete=models.CASCADE, related_name='taken_from')
    return_to = models.ForeignKey(PickUpPoint, on_delete=models.CASCADE, related_name='return_to')

    def __str__(self):
        return str(self.issue_datetime) + ' ' + str(self.car)