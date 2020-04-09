from django.db import models


class Avtom(models.Model):
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    dateo = models.DateTimeField('date')


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = [
        ("M", "Man"),
        ("W", "Women"),
    ]
    passportnum = models.IntegerField()
    dates = models.ManyToManyField(Avtom, through='Mej')


class Mej(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avto = models.ForeignKey(Avtom, on_delete=models.CASCADE)
    buyd = models.DateField()
    selld = models.DateField()


class Vodud(models.Model):
    number = models.CharField(max_length=20)
    types = models.CharField(max_length=20)
    date = models.DateField('datebuy')
    users = models.ForeignKey(User, on_delete=models.CASCADE)


