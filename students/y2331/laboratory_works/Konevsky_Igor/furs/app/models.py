from django.db import models
from django.urls import reverse


class Farm(models.Model):
    farm_id = models.IntegerField(primary_key=True)
    adress = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()

    object = models.Manager()

    #def get_absolute_url(self):
     #   return reverse('', args=[str(self.farm_id)])


class Fur(models.Model):
    fur_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sort = models.CharField(max_length=50)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    object = models.Manager()

class Buyer(models.Model):
    CATEG = [
        ('Factory', 'Factory'),
        ('Studio', 'Studio'),
        ('Person', 'Person')
    ]
    buyer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEG)

    object = models.Manager()

class Purchase(models.Model):
    purchase_id = models.IntegerField(primary_key=True)
    amount = models.IntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    fur = models.ForeignKey(Fur, on_delete=models.CASCADE)

    object = models.Manager()