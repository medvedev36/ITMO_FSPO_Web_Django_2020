from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

# Create your models here.


class Client(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    purchases = models.ManyToManyField('InDeals')


class Broker(models.Model):
    name_brok = models.CharField(max_length=100)
    Birthday = models.DateField()
    phone_brok = models.CharField(max_length=11, blank=True)
    address_brok = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name_brok


class Product(models.Model):
    name_prod = models.CharField(max_length=100)
    exp_date = models.DateField()
    about_prod = models.TextField()

    def __str__(self):
        return self.name_prod

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={"pk": self.pk})


class Provider(models.Model):

    name_prov = models.CharField(max_length=100)
    address_prov = models.CharField(max_length=100, blank=True)
    date_auth = models.DateField()
    prov_about = models.TextField()

    def __str__(self):
        return self.name_prov

    def get_absolute_url(self):
        return reverse('provider-detail', kwargs={"pk": self.pk})


class Deals(models.Model):
    code_deal = models.CharField(max_length=4, default='0')
    date_deal = models.DateField()
    col_sold = models.IntegerField()
    CATEGORY = (
        ('N', 'New'),
        ('U', 'Unon'),
        ('B', 'Bad'),
    )
    view_prod = models.CharField(max_length=1, choices=CATEGORY, default='U')
    br_name = models.ForeignKey(Broker, on_delete=models.CASCADE)
    prod_name = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.code_deal

    def get_absolute_url(self):
        return reverse('home')


class InDeals(models.Model):
    date_deal = models.DateField()
    deals = models.ForeignKey(Deals, on_delete=models.CASCADE)

    def __str__(self):
        return '{} '.format(self.deals)


class Supplier(models.Model):
    code_supp = models.CharField(max_length=4, default='0')
    price_sold = models.IntegerField()
    date_supp = models.DateField()
    col_supp = models.IntegerField()
    prov_name = models.ForeignKey(Provider, on_delete=models.CASCADE)
    prod_name = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.code_supp
