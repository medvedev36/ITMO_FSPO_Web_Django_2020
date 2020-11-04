from django.db import models


# Create your models here.
class Cassette(models.Model):
    title = models.CharField(max_length=60)
    theme = models.CharField(max_length=45)
    director = models.CharField(max_length=60)
    release_date = models.DateField()
    studio = models.CharField(max_length=60)


class Seller(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    address = models.CharField(max_length=120)


class Provider(models.Model):
    title = models.CharField(max_length=60)
    address = models.CharField(max_length=120)


class CassetteArriving(models.Model):
    cassette = models.ForeignKey(Cassette, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField()
    quantity = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


class CassetteSelling(models.Model):
    cassette = models.ForeignKey(Cassette, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField()
    quantity = models.IntegerField()
    client = models.CharField(max_length=120)
