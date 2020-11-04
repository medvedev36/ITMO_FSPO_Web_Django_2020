from django.contrib.auth.models import AbstractUser
from django.db import models

from .choices import USER_TYPE_CHOICE

class MyUser(AbstractUser):
    image = models.ImageField(upload_to='pic_users', default='user_default.jpg')
    points = models.PositiveIntegerField(default=0)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICE, default=1)
    trips = models.ManyToManyField('Ride', through='Ticket')

