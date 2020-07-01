from django.db import models

class Channel(models.Model):
    channel_name = models.CharField("Название", max_length=45)

    class Meta:
        verbose_name = "Канал"
        verbose_name_plural = "Каналы"

class TVShow(models.Model):
    time = models.TimeField("Время выхода в эфир")
    cost = models.FloatField("Стоимость показа за минуту")
    show_name = models.CharField("Название", max_length=45)
    idChannel = models.ForeignKey(Channel, verbose_name="Номер канала", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

class Advertiser(models.Model):
    discount = models.FloatField("Скидка за показ", blank=True, null=True)
    advertiser_name = models.CharField("Название", max_length=45)

    class Meta:
        verbose_name = "Рекламная компания"
        verbose_name_plural = "Рекламные компании"

class Advertising(models.Model):
    adName = models.CharField("Название", max_length=45)
    time = models.IntegerField("Время ролика")
    idAdvertiser = models.ForeignKey(Advertiser, verbose_name="Рекламная компания", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ролик"
        verbose_name_plural = "Ролики"

class AdBreak(models.Model):
    date = models.DateTimeField("Дата показа", blank=True, null=True)
    idTVShow = models.ForeignKey(TVShow, verbose_name="ТВ программа", on_delete=models.CASCADE)
    idAdvertising = models.ForeignKey(Advertising, verbose_name="Ролик", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Показ ролика"
        verbose_name_plural = "Показы ролика"
