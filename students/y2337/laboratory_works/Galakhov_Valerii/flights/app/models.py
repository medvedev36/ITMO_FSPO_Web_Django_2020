from django.db import models


class Helicopter(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название модели")
    carryingCapacity = models.FloatField(verbose_name="Максимальная грузоподъёмность, т")
    dateOfProduction = models.DateField()

    def __str__(self):
        return str(self.name)


class Pilot(models.Model):
    idHelicopter = models.ForeignKey(Helicopter, verbose_name="Вертолёт", on_delete=models.CASCADE)
    pilotName = models.CharField(max_length=30, verbose_name="Имя пилота")
    pilotPost = models.CharField(max_length=30, verbose_name="Должность")
    pilotExperience = models.PositiveIntegerField(verbose_name="Стаж")
    dateOfBirth = models.DateField()

    def __str__(self):
        return str(self.pilotName)


class Flight(models.Model):
    idHelicopter = models.ForeignKey(Helicopter, verbose_name="Вертолёт", on_delete=models.CASCADE)
    dateOfFlight = models.DateField()
    cargoWeight = models.PositiveIntegerField(verbose_name="Масса перевезённого груза, т")
    flightDuration = models.PositiveIntegerField(verbose_name="Длительность рейса, ч")
    flightCost = models.PositiveIntegerField(verbose_name="Стоимость рейса")

    def __str__(self):
        return str(self.id)


