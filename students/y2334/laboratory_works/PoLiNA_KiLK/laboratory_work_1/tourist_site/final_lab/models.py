from django.db import models

# Create your models here.


class Routes(models.Model):
    Name = models.CharField("Название пути", max_length=45, primary_key=True)
    Start = models.CharField("Точка старта", max_length=45, null=False)
    Finish = models.CharField("Точка финиша", max_length=45, null=False)
    Duration = models.IntegerField("Протяженность в километрах")

    def __str__(self):
        return self.Name


class Buses(models.Model):
    DoesNotExist = None
    objects = None
    Number = models.CharField("Номер автобуса", max_length=45, primary_key=True)
    Name = models.CharField("Название автобуса", max_length=45, null=False)
    Total_run = models.IntegerField("Пробег", null=True)

    def __str__(self):
        return self.Number


class Staff(models.Model):
    objects = None
    DoesNotExist = None
    Driver_license = (
        ('A', 'Мотоциклы'),
        ('A1', 'Легкие мотоциклы'),
        ('B', 'Легкие автомобили'),
        ('B1', 'Трициклы и квадроциклы'),
        ('C', 'Грузовики'),
        ('C1', 'Грузовики'),
        ('D', 'Автобусы'),
        ('D1', 'Автобусы'),
        ('BE', 'Владение легковесным прицепом'),
        ('CE', 'Владение тяжеловесным прицепом'),
        ('C1E', 'Грузовики подкатегории C1'),
        ('DE', 'Автобусы с прицепом'),
        ('D1E', 'Автобусы подкатегории D1'),
        ('M', 'Мопеды и квадроциклы'),
        ('Tm', 'Трамваи'),
        ('Tb', 'Троллейбусы')
    )

    Table_number = models.AutoField("Табличный номер", primary_key=True, auto_created = True, serialize = False)
    Experience = models.IntegerField("Стаж вождения", null=True)
    Category = models.CharField("Типы транспорта", max_length=3, choices=Driver_license, blank=False)
    Address = models.CharField("Адрес проживания", max_length=50, null=False)
    Birth_year = models.DateField("Дата рождения", max_length=4)
    Number_b = models.ForeignKey(Buses, null=True, on_delete=models.SET_NULL, related_name='number_bus', verbose_name="Номер автобуса")
    Second_name = models.CharField("Фамилия", max_length=30, null=False)

    def __str__(self):
        return self.Address


class Ways(models.Model):
    ID_way = models.AutoField("Идентификатор маршрута", primary_key=True)
    Start_date = models.DateField("Дата начала поездки", max_length=4)
    Finish_date = models.DateField("Дата конца поездки", max_length=4)
    Passengers = models.IntegerField("Колличество пасажиров")
    Ticket_cost = models.IntegerField("Стоимость билета")
    Name = models.ForeignKey(Routes, null=True, blank=True, on_delete=models.SET_NULL, related_name='name', verbose_name="Название маршрута")
    Number = models.ForeignKey(Buses, null=True, blank=True, on_delete=models.SET_NULL, related_name='number', verbose_name="Номер автобуса")
    Done_flag = models.BooleanField("Статус завершенности", default=False)

    def __str__(self):
        return self.ID_way


class Cities(models.Model):
    ID_TR = models.AutoField("Идентификатор пути", primary_key=True)
    Name = models.ForeignKey(Routes, null=True, on_delete=models.SET_NULL, related_name='Name_route', verbose_name="Название маршрута")
    Towns = models.CharField("Город", max_length=30, null=False)

    def __str__(self):
        return self.ID_TR