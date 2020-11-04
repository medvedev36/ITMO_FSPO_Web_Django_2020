from django.db import models
from django.utils import timezone

# Create your models here.
class Trawler(models.Model):
    trawler_id = models.IntegerField(primary_key=True, unique=True)
    tname = models.CharField(max_length=40)
    displacement = models.IntegerField()
    prod_date = models.DateField()


class Voyage(models.Model):
    voyage_id = models.IntegerField(primary_key=True, unique=True)
    trawler_id = models.ForeignKey(Trawler, blank=False, null=False, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    bank_name = models.CharField(max_length=40)
    fish_name = models.CharField(max_length=40)
    fish_quantity = models.IntegerField()


class Crew(models.Model):
    member_id = models.IntegerField(primary_key=True, unique=True)
    trawler_id = models.ForeignKey(Trawler, blank=False, null=False, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=40)
    member_job = models.CharField(max_length=40)
    hire_date = models.DateField()
    bday = models.DateField()
    to_pension = models.DateField()