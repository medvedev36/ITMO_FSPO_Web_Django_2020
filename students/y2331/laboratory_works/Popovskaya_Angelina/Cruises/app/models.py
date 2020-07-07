from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    photo = models.TextField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Cruise(models.Model):
    name = models.CharField(max_length=50)
    reg_number = models.IntegerField()
    price_1 = models.DecimalField(max_digits = 6, decimal_places=2)
    price_2 = models.DecimalField(max_digits=6, decimal_places=2)
    price_3 = models.DecimalField(max_digits=6, decimal_places=2)
    name_captain = models.CharField(max_length=50)


class Excursion(models.Model):
    id_cruise = models.IntegerField()
    date_of_departure = models.DateField()
    date_of_arrival = models.DateField()
    quantity_post_of_1 = models.IntegerField()
    quantity_post_of_2 = models.IntegerField()
    quantity_post_of_3 = models.IntegerField()
    information = models.TextField()
    photo = models.TextField()


class Sell(models.Model):
    id_excursion = models.IntegerField()
    id_profile = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

# Create your models here.
