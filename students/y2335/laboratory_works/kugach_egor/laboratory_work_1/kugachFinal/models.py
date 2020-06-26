from django.db import models


# Create your models here.

class Author(models.Model):
    last_name = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    patronymic = models.CharField(max_length=50, blank=True, null=True)


class Category(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)


class Book(models.Model):
    ISBN = models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    pagesCount = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publicationDate = models.DateTimeField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return "%s" % self.title


class Orders(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    count = models.IntegerField()
    email = models.EmailField(blank=True, null=True)


class Edition(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.IntegerField()
    count_of_book = models.IntegerField()
