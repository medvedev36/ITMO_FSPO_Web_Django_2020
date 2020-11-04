from django.db import models



class Farm(models.Model):
    farm_id = models.IntegerField(primary_key=True)
    adress = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()




class Fur(models.Model):
    fur_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sort = models.CharField(max_length=50)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    price = models.IntegerField()


class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    fur = models.ForeignKey(Fur, on_delete=models.CASCADE)
    object = models.Manager()


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    fur = models.ForeignKey(Fur, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    user_id = models.IntegerField(default=0)
    object = models.Manager()
