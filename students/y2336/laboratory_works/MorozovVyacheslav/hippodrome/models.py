from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Horse(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    experience = models.IntegerField()
    owner = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Jockey(AbstractUser):
    image = models.ImageField(upload_to='profile_pics', default='default_user.jpg')
    experience = models.IntegerField(null=True, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username

class Crew(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    jockey = models.ForeignKey(Jockey, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.jockey, self.horse)

class Hippodrome(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    people_capacity = models.IntegerField()
    website = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.address, self.name)

class Competition(models.Model):
    fund = models.IntegerField()
    name = models.CharField(max_length=100)
    date = models.DateField()
    participants = models.ManyToManyField(Crew, through='Race')
    hippodrome = models.ForeignKey(Hippodrome, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Race(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    place = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.crew, self.place)