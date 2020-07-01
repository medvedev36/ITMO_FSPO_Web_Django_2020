from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Board(models.Model):
  title = models.CharField(max_length=80)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='board')

class Panel(models.Model):
  title = models.CharField(max_length=80)
  index = models.IntegerField()
  board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='panel')
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='panel')

class Card(models.Model):
  value = models.CharField(max_length=255)
  index = models.IntegerField()
  panel = models.ForeignKey(Panel, on_delete=models.CASCADE, null=True, related_name='card')
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='card')

  