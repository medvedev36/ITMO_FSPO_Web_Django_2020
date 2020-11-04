from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    passport_number = models.IntegerField(unique=True, null=True)
    address = models.CharField(max_length=150, null=True)
    nationality = models.CharField(max_length=30, null=True)


class Car(models.Model):
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    number = models.CharField(max_length=10)

    def get_absolute_url(self):
        return u'/car/%d' % self.id
    # owners = models.ManyToManyField(Owner, through='Ownership')


class Owner(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    birthday = models.DateField()
    cars = models.ManyToManyField(Car, through='Ownership')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class License(models.Model):
    LICENSE_CATEGORIES = (
        ('A', 'Мотоциклы'),
        ('A1', 'Легкие мотоциклы'),
        ('B', 'Легковые автомобили, небольшие грузовики (до 3,5 тонн)'),
        ('BE', 'Легковые автомобили с прицепом'),
        ('B1', 'Трициклы'),
        ('C', 'Грузовые автомобили (от 3,5 тонн)'),
        ('CE', 'Грузовые автомобили с прицепом'),
        ('C1', 'Средние грузовики (от 3,5 до 7,5 тонн)'),
        ('C1E', 'Средние грузовики с прицепом'),
        ('D', 'Автобусы'),
        ('DE', 'Автобусы с прицепом'),
        ('D1', 'Небольшие автобусы'),
        ('D1E', 'Небольшие автобусы с прицепом'),
        ('M', 'Мопеды'),
        ('Tm', 'Трамваи'),
        ('Tb', 'Троллейбусы'),
    )
    number = models.IntegerField()
    issue_date = models.DateField()
    category = models.CharField(max_length=3, choices=LICENSE_CATEGORIES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
