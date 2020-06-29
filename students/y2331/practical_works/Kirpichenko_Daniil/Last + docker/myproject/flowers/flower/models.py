from django.db import models
from django.shortcuts import reverse
# Create your models here.


COUNTRIES = [
    ('RU', 'Russia'),
    ('UKR', 'Ukraine'),
    ('BLR', 'Belarus')
]


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True, unique=True)
    client_last_name = models.CharField(max_length=30, blank=True, null=True)
    client_first_name = models.CharField(max_length=30, blank=True, null=True)
    client_address = models.CharField(max_length=30, blank=True, null=True)
    client_city = models.CharField(max_length=30, blank=True, null=True)
    client_country = models.CharField(max_length=3, choices=COUNTRIES, default="RU")
    client_phone_number = models.IntegerField(null=True, blank=True)
    client_credit_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.client_id)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True, unique=True)
    employee_first_name = models.CharField(max_length=30, blank=True, null=True)
    employee_last_name = models.CharField(max_length=30, blank=True, null=True)
    employee_position = models.CharField(max_length=30, blank=True, null=True)
    employee_address = models.CharField(max_length=30, blank=True, null=True)
    employee_city = models.CharField(max_length=30, blank=True, null=True)
    employee_country = models.CharField(max_length=3, choices=COUNTRIES, default="RU")
    employee_phone_number = models.IntegerField(null=True, blank=True)
    employee_hiring_date = models.DateField()
    employee_birthday_date = models.DateField()
    employee_orders = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.employee_id)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, unique=True)
    order_client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, default=0)
    order_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, default=0)
    order_date = models.DateField(default='2020-01-01')
    order_completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.order_id)


class ProductCategories(models.Model):
    category_name = models.CharField(max_length=30, primary_key=True,default="default")

    def __str__(self):
        return '{}'.format(self.category_name)


class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True, unique=True)
    provider_organization = models.CharField(max_length=30, blank=True, null=True)
    provider_first_name = models.CharField(max_length=30, blank=True, null=True)
    provider_last_name = models.CharField(max_length=30, blank=True, null=True)
    provider_position = models.CharField(max_length=30, blank=True, null=True)
    provider_phone_number = models.IntegerField(null=True, blank=True)
    provider_address = models.CharField(max_length=30, blank=True, null=True)
    provider_city = models.CharField(max_length=30, blank=True, null=True)
    provider_country = models.CharField(max_length=3, choices=COUNTRIES, default="RU")

    def __str__(self):
        return '{}'.format(self.provider_id)


class Products(models.Model):
    product_id = models.AutoField(primary_key=True, unique=True)
    product_name = models.CharField(max_length=30, blank=True, null=True)
    product_provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    product_count = models.IntegerField(null=True, blank=True)
    product_cost = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('flower_detail_url', kwargs={'flower_id': self.product_id})

    def __str__(self):
        return '{}'.format(self.product_id)


class OrderInformation(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_product_count = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = (("order_id", "product_id"),)
