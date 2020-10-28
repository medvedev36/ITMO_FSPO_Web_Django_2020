from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from decimal import Decimal
from django.core.validators import MinValueValidator
from datetime import datetime


# Create your models here.


class Client(AbstractUser):
    phone_num = models.CharField(max_length=20, blank=True, verbose_name='Phone number')
    address = models.CharField(max_length=100, blank=True, verbose_name='Address')
    purchases = models.ManyToManyField('InDeals')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Broker(models.Model):
    name_brok = models.CharField(max_length=100, verbose_name='Broker name')
    birthday = models.DateField(verbose_name='Date of birth')
    phone_brok = models.CharField(max_length=11, blank=True, verbose_name='Broker phone')
    address_brok = models.CharField(max_length=100, blank=True, verbose_name='Broker address')

    class Meta:
        verbose_name = 'Broker'
        verbose_name_plural = 'Brokers'

    def __str__(self):
        return self.name_brok


class CD(models.Model):
    name_cd = models.CharField(max_length=100, verbose_name='CD name')
    prod_date = models.DateField(verbose_name='Production date')
    descr = models.CharField(max_length=100, blank=True, null=True, verbose_name='Description')

    class Meta:
        verbose_name = 'CD'
        verbose_name_plural = 'CDs'
        ordering = ('-prod_date',)

    def __str__(self):
        return self.name_cd

    def get_absolute_url(self):
        return reverse('cd-detail', kwargs={"pk": self.pk})


class Game(models.Model):
    name = models.CharField(primary_key=True, max_length=100, verbose_name='Name')
    genre = models.CharField(max_length=85, blank=True, null=True, verbose_name='Genre')
    author = models.CharField(max_length=55, verbose_name='Author')
    cd_name = models.ForeignKey(CD, on_delete=models.CASCADE, verbose_name='CD name')

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'


class Firm(models.Model):
    name_sup = models.CharField(max_length=100)
    address_sup = models.CharField(max_length=100, blank=True)
    sup_about = models.TextField()

    class Meta:
        verbose_name = 'Firm'
        verbose_name_plural = 'Firms'

    def __str__(self):
        return self.name_sup

    def get_absolute_url(self):
        return reverse('firm-detail', kwargs={"pk": self.pk})


class Deal(models.Model):
    code_deal = models.CharField(max_length=4, default='0', verbose_name='Deal code')
    date_deal = models.DateField(default=datetime.now, verbose_name='Date deal')
    quantity_sale = models.PositiveIntegerField(verbose_name='Sale quantity')
    br_name = models.ForeignKey(Broker, on_delete=models.CASCADE, verbose_name='Broker id')
    cd_name = models.ForeignKey(CD, on_delete=models.CASCADE, verbose_name='CD id')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client name')

    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'

    def __str__(self):
        return self.code_deal

    def get_absolute_url(self):
        return reverse('home')


class InDeals(models.Model):
    date_deal = models.DateField(default=datetime.now, verbose_name='Deal date')
    deals = models.ForeignKey(Deal, on_delete=models.CASCADE, verbose_name='Deal id')

    def __str__(self):
        return '{} '.format(self.deals)


class Supply(models.Model):
    code_supp = models.CharField(max_length=4, default='0', verbose_name='Supply code')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))],
                                verbose_name='Price')
    date_supp = models.DateField(default=datetime.now, verbose_name='Supply date')
    quantity_ad = models.PositiveIntegerField(verbose_name='Admission quantity')
    sup_name = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name='Supplier name')
    cd_name = models.ForeignKey(CD, on_delete=models.CASCADE, verbose_name='CD name')

    class Meta:
        verbose_name = 'Supply'
        verbose_name_plural = 'Supplies'

    def __str__(self):
        return self.code_supp
