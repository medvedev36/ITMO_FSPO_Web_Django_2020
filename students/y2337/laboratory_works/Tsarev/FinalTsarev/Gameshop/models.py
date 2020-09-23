from django.db import models

# Create your models here.


class Disc(models.Model):
    disc_id = models.IntegerField(primary_key=True, unique=True)
    disc_name = models.CharField(max_length=70)
    production_date = models.DateField()
    firm = models.CharField(max_length=70)
    url = models.URLField()
    genres = models.ManyToManyField('Genre', verbose_name="Жанры", related_name="discs")
    games = models.ManyToManyField('Game', verbose_name="Игры", related_name="discs")
    description = models.TextField()

    class Meta:
        verbose_name = "Диск"
        verbose_name_plural = "Диски"

    def __str__(self):
        return self.disc_name


class Buy(models.Model):
    buy_id = models.IntegerField(primary_key=True, unique=True)
    date_buy = models.DateField()
    amount = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    disc = models.ForeignKey(Disc, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    def __str__(self):
        return self.buy_id


class Sale(models.Model):
    sale_id = models.IntegerField(primary_key=True, unique=True)
    date_sale = models.DateField()
    amount = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    disc = models.ForeignKey(Disc, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return self.sale_id


class Game(models.Model):
    game_id = models.IntegerField(primary_key=True, unique=True)
    game_name = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    url = models.URLField()

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        return self.game_name


class Author(models.Model):
    au_id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.last_name


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True, unique=True)
    genre_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre_name


