from django.db import models
from datetime import datetime


class CashInformation(models.Model):
    balance = models.IntegerField(default=0)
    date_addition = models.DateTimeField(default=datetime.now)


class User(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    telephone_number = models.IntegerField(default=0)
    cash_information = models.ForeignKey(CashInformation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rate(models.Model):
    user_zone_code = models.IntegerField(default=0)
    call_zone_code = models.IntegerField(default=0)
    call_price_per_minute = models.IntegerField(default=0)
    user_zone_name = models.CharField(max_length=50)
    call_zone_name = models.CharField(max_length=50)


class CallInformation(models.Model):
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)
    price = models.IntegerField(default=0)
    users = models.ManyToManyField(User, through='UserCall')


class UserCall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    call = models.ForeignKey(CallInformation, on_delete=models.CASCADE)
    pay_date = models.DateField(default=datetime.now, blank=True, null=True)
    is_paid = models.BooleanField(default=0)


class Account(models.Model):
    login = models.SlugField(max_length=20)
    password = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
