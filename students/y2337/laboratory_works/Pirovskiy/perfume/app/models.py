from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название Компании")

    def __str__(self):
        return str(self.name)


class Mackler(models.Model):
    idMac = models.ForeignKey(Company, verbose_name="Компания-Наниматель", on_delete=models.CASCADE)
    surMac = models.CharField(max_length=30, verbose_name="Фамилия Маклера")
    adrMac = models.CharField(max_length=30, verbose_name="Адресс Маклера")

    def __str__(self):
        return str(self.surMac)


class Product(models.Model):
    variants = {
        ("Парфюм", "Парфюм"),
        ("Шампунь", "Шампунь"),
        ("Туалетная вода", "Туалетная вода"),
    }
    nameProd = models.CharField(max_length=30, verbose_name="Название продукта")
    varProd = models.CharField(max_length=30, choices=variants, verbose_name="Тип Товара")
    priceProd = models.PositiveIntegerField(verbose_name="Цена Продукта")
    idComp = models.ForeignKey(Company, verbose_name="Компания-Поставщик", on_delete=models.CASCADE)
    expProd = models.DateField()

    def __str__(self):
        return str(self.nameProd)
