from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class Client(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True)


class Attraction(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    lifetime = models.IntegerField(max_length=2)
    start_year = models.IntegerField(max_length=4)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attraction_detail', kwargs={"pk": self.pk})


class Platform(models.Model):
    address = models.CharField(max_length=100)
    fio_ceo = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.address


class Relationship(models.Model):
    Date_of_owning = models.DateField()
    platform_id = models.ForeignKey('Platform', on_delete=models.CASCADE)
    attraction_id = models.ForeignKey('Attraction', on_delete=models.CASCADE)


class Price(models.Model):
    price_kids = models.IntegerField(max_length=4)
    price_adult = models.IntegerField(max_length=4)
    price_privilege = models.IntegerField(max_length=4)
    Relationship_id = models.ForeignKey('Relationship', on_delete=models.CASCADE)


class Operation(models.Model):
    date_operation = models.DateField(auto_now_add=True)
    kids = models.IntegerField(blank=True, max_length=4)
    adults = models.IntegerField(blank=True, max_length=4)
    privilege = models.IntegerField(blank=True, max_length=4)
    Relationship_id = models.ForeignKey('Relationship', on_delete=models.CASCADE)

# Create your models here.
