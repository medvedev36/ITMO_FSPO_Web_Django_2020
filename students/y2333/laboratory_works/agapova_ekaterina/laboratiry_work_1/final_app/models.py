from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    """Расширенная модель пользователя"""
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    card = models.CharField(max_length=20, default=None, blank=True, null=True)
    email = models.CharField(max_length=50)


class Fabric(models.Model):
    """Модель производителя"""
    address = models.CharField(max_length=500)
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=50)


class Product(models.Model):
    """Модель продукта"""
    price = models.FloatField()
    name = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=50)
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    image = models.CharField(max_length=300)


class Delivery(models.Model):
    """Модель поставок"""
    delivery_date = models.DateField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_for_sale = models.FloatField()


class Sale(models.Model):
    """Модель продаж"""
    date = models.DateTimeField(auto_now_add=True, blank=True)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
