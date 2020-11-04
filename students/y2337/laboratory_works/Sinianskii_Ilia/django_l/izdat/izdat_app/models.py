from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Author(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)


class Book(models.Model):
    title = models.CharField(max_length=45)
    category_code = models.CharField(max_length=45)
    number_of_pages = models.IntegerField()
    year_of_publication = models.IntegerField()
    isbn_kode = models.IntegerField()
    author_has_book = models.ManyToManyField(Author)
    price = models.FloatField(default=0)


class Edition(models.Model):
    numbers_of_copies = models.IntegerField()
    date = models.DateField()
    price = models.FloatField(default=0)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone_num = models.IntegerField()


class Order(models.Model):
    date = models.DateField()
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Book_has_Order = models.ManyToManyField(Book)
