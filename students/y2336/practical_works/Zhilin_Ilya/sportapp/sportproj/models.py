from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from datetime import date


class Competition(models.Model):
    title = models.CharField(max_length=50, default=None)
    date = models.DateField()
    place = models.CharField(max_length=50, default=None)
    category = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('competitions_form', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class Trainer(models.Model):
    name = models.CharField(max_length=100, default=None)
    phone = models.IntegerField(default=0)
    category = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('trainers_form', kwargs={'id': self.id})

    def __str__(self):
        return self.name


class Sportsman(models.Model):
    name = models.CharField(max_length=100, default=None)
    category = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('sportsmen_form', kwargs={'id': self.id})

    def __str__(self):
        return self.name


class Trauma(models.Model):
    sportsman = models.ForeignKey(
        Sportsman, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=100, default=None)

    def get_absolute_url(self):
        return reverse('traumas_form', kwargs={'id': self.id})


class Contest(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, null=True, blank=True)
    sportsman = models.ForeignKey(
        Sportsman, on_delete=models.CASCADE, null=True, blank=True)
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, null=True, blank=True)
    sportsman_position = models.IntegerField(default=0)
    sportsman_score = models.IntegerField(default=0)
    trainer_score = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('contest_form', kwargs={'id': self.id})


class Workout(models.Model):
    sportsman = models.ForeignKey(
        Sportsman, on_delete=models.CASCADE, null=True, blank=True)
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=date.today())


class User(AbstractUser):
    sportsman = models.ForeignKey(
        Sportsman, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
