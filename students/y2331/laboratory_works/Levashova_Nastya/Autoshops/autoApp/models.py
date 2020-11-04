from django.db import models
from django.contrib.auth.models import User

class Car_Models(models.Model):
    model_name = models.CharField("Марка авто", max_length=30)
    engine_capacity = models.FloatField("Объем двигателя")
    engine_power = models.FloatField("Мощность двигателя")

    class Meta:
        verbose_name = "Модель авто"
        verbose_name_plural = "Модели авто"

class Autoshops(models.Model):
    address = models.CharField("Адрес", max_length=100)
    shop_name = models.CharField("Название", max_length=45)
    car_models = models.ManyToManyField(Car_Models, verbose_name="Обслуживаемые марки авто")

    class Meta:
        verbose_name = "Автомастерская"
        verbose_name_plural = "Автомастерские"

class Masters(models.Model):
    full_name_m = models.CharField("ФИО", max_length=50)
    phone_number = models.CharField("Номер телефона", max_length=12)
    shop_number = models.ForeignKey(Autoshops, verbose_name="Автомастерская", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

class Costumer(models.Model):
    full_name_c = models.CharField("ФИО", max_length=50)
    address_c = models.CharField("Адрес", max_length=100)
    phone_number_c = models.CharField("Номер телефона", max_length=12)
    passport = models.IntegerField("Серия и номер паспорта", max_length=10)

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"

class Cars(models.Model):
    state_number = models.CharField("Госномер", max_length=9, primary_key=True)
    year_of_issue = models.DateField("Год выпуска")
    date_sheet_number = models.IntegerField("Номер техпаспорта", max_length=6)
    model_id = models.ForeignKey(Car_Models, verbose_name="Марка авто", on_delete=models.CASCADE)
    costumer_id = models.ForeignKey(Costumer, verbose_name="Владелец авто", on_delete=models.CASCADE, related_name="custumer")

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

class Comprehensive_Repair(models.Model):
    state_number_r = models.ForeignKey(Cars, verbose_name="Госномер авто", on_delete=models.CASCADE)
    comrepair_date = models.DateField("Дата регистрации комплексного ремонта", auto_now_add=True)

    class Meta:
        verbose_name = "Комплексный ремонт"
        verbose_name_plural = "Комплексные ремонты"

class Completed_Works(models.Model):
    type_of_repair = models.CharField("Вид ремонта", max_length=40, choices=[
        ('Замена отдельных элементов кузова', 'Replacing individual body elements'),
        ('Подбор краски и покраска', 'Selecting paint and painting'),
        ('Замена ремней', 'Replacing belts'),
        ('Регулировка клапанов', 'Adjusting valves'),
        ('Замена маслосъёмных колпачков', 'Replacing oil scraper caps'),
        ('Замена ведущих и ведомых шестерен', 'Replacing drive and driven gears'),
        ('Замена масел', 'Replacing oil'),
        ('Замена фильтров', 'Replacing filters'),
    ])
    receipt_date = models.DateTimeField("Дата поступления авто на ремонт", auto_now_add=True)
    repair_completion_date = models.DateField("Дата завершения ремонта", blank=True, null=True)
    repair_cost = models.FloatField("Стоимость", null=True)
    shop_number_w = models.ForeignKey(Autoshops, verbose_name="Автомастерская", on_delete=models.CASCADE)
    state_number_w = models.ForeignKey(Cars, verbose_name="Госномер авто", on_delete=models.CASCADE)
    master_id = models.ForeignKey(Masters, verbose_name="Мастер", on_delete=models.CASCADE)
    comrepair_id = models.ForeignKey(Comprehensive_Repair, verbose_name="Комплексный ремонт", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Ремонтная работа"
        verbose_name_plural = "Ремонтные работы"

