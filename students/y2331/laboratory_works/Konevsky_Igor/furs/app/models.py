from django.db import models
from django.urls import reverse


class Farm(models.Model):
    farm_id = models.IntegerField(primary_key=True)
    adress = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()

    object = models.Manager()


class Fur(models.Model):
    fur_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sort = models.CharField(max_length=50)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    object = models.Manager()


class Coat(models.Model):
    coat_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    fur = models.ForeignKey(Fur, on_delete=models.CASCADE)

    object = models.Manager()


class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    coat = models.ForeignKey(Coat, on_delete=models.CASCADE)

    object = models.Manager()


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    coat = models.ForeignKey(Coat, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    object = models.Manager()

