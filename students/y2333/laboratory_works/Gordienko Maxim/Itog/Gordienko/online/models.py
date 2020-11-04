from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

# Create your models here.
class Customer(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    purchases = models.ManyToManyField('InStock', through='Purchase')

    def __str__(self):
        return self.username


class Brand(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand-detail', kwargs={"pk": self.pk})


class Store(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50)
    products = models.ManyToManyField('Product', through='InStock')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={"pk": self.pk})


class InStock(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.store, self.product)


class Purchase(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    instock = models.ForeignKey(InStock, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.customer, self.instock.product)

