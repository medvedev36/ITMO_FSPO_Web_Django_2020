from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Playground(models.Model):
  image = models.ImageField(null=True)
  address_playground = models.CharField(max_length=90)
  last_name = models.CharField(max_length=45)

class AttractionType(models.Model):
  attraction_type = models.CharField(max_length=45)

class Attraction(models.Model):
  image = models.ImageField(null=True)
  name_attraction = models.CharField(max_length=45)
  year_purchase = models.IntegerField()
  old = models.IntegerField()
  adult_price = models.IntegerField()
  children_price = models.IntegerField()
  type = models.ForeignKey(AttractionType, on_delete=models.SET_NULL, null=True, related_name='attraction')

class Use_attraction(models.Model):
  date = models.DateTimeField()
  adult_ticket = models.IntegerField(default=0)
  children_ticket = models.IntegerField(default=0)
  attraction = models.OneToOneField(Attraction, on_delete=models.CASCADE, null=False, related_name='useAttraction')
  playground = models.ForeignKey(Playground, on_delete=models.CASCADE, null=False, related_name='useAttraction')

class My_purchase(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='my_purchase')
  attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, null=False, related_name='my_purchase')
  price = models.IntegerField()
  date = models.DateField(default=datetime.now, blank=True)