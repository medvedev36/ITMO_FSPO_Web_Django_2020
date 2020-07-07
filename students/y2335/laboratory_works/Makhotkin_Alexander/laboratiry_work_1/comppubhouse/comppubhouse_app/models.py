from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=False)


class Author(models.Model):
    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=20, null=False)
    patronymic = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=45, null=True)


class Customer(AbstractUser):
    address = models.CharField(max_length=80, null=True)
    phone_number = models.CharField(max_length=12, null=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    date_order = models.DateTimeField(auto_now=False, null=True)
    bought = models.BooleanField(null=False, default=False)


class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    authors = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100, null=False)
    pages = models.DecimalField(max_digits=4, decimal_places=0, null=False)
    published = models.DateField(null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    count = models.DecimalField(max_digits=5, decimal_places=0, null=False, default=0)
    in_orders = models.ManyToManyField(Order, through='BooksInOrder')


class BooksInOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    count = models.DecimalField(max_digits=5, decimal_places=0, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False)


class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=300, null=False)
    date = models.DateTimeField(auto_now=True, null=False)
    score = models.DecimalField(max_digits=2, decimal_places=0, null=False, default=10)


class Circulation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False)
    count = models.DecimalField(max_digits=5, decimal_places=0, null=False)
