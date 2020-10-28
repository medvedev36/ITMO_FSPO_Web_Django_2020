from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя автора")
    dateOfBirth = models.DateField()

    def __str__(self):
        return str(self.name)


class Music(models.Model):
    idAuthor = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)
    musicName = models.CharField(max_length=30, verbose_name="Название композиции")

    def __str__(self):
        return str(self.musicName)


class Producer(models.Model):
    COUNTRIES = (
        ('Россия', 'Россия'),
        ('США', 'США'),
        ('Франция', 'Франция'),
        ('Швеция', 'Швеция'),
        ('Турция', 'Турция')
    )
    name = models.CharField(max_length=30, verbose_name="Название производителя")
    country = models.CharField(max_length=30, choices=COUNTRIES, verbose_name="Страна производителя")

    def __str__(self):
        return str(self.name)


class Disk(models.Model):
    incomeCost = models.PositiveIntegerField(verbose_name="Цена")
    idMusic = models.ForeignKey(Music, verbose_name="Композиция", on_delete=models.CASCADE)
    idProducer = models.ForeignKey(Producer, max_length=30, on_delete=models.CASCADE, verbose_name="Производитель")

    def __str__(self):
        return str(self.id)


