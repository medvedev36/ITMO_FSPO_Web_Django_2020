from django.db import models
from django.contrib.auth.models import User


# from djoser.urls.base import User


class Model_of_car(models.Model):
    """Модель автомобиля"""
    model = models.CharField("Модель", max_length=45, primary_key=True)
    brand = models.CharField("Брэнд", max_length=45)
    carrying = models.IntegerField("Грузоподъемность")


class Cars(models.Model):
    """Автомобили"""
    license_plate = models.CharField(max_length=6, primary_key=True)
    model = models.ForeignKey(Model_of_car, on_delete=models.CASCADE)
    run = models.FloatField()


class Drivers(models.Model):
    """Водители"""
    CATEGORY = [
        ('A', 'Motorcycle'),
        ('B', 'Car'),
        ('C', 'Truck'),
        ('D', 'Bus'),
        ('M', 'Moped'),
    ]
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45, null=True)
    category = models.CharField(max_length=1, choices=CATEGORY, default='B')
    experience = models.IntegerField()
    address = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Manifests(models.Model):
    """Путевые листы"""
    date = models.DateField()
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)


class Clients(models.Model):
    """Клиенты"""
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)


class Items(models.Model):
    """Товары"""
    name = models.CharField(max_length=45)


class Orders(models.Model):
    """Заказы"""
    DIRECT = [
        ('From client', 'From client'),
        ('To client', 'To client'),
    ]
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    direction = models.CharField(max_length=11, choices=DIRECT, default='From client')
    kilometrage = models.FloatField()
    weight = models.FloatField()
    price = models.FloatField()
    second_point = models.CharField(max_length=45)
    manifest = models.ForeignKey(Manifests, null=True, on_delete=models.CASCADE)


class Order_composition(models.Model):
    """Состав заказа"""
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField()
