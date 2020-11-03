# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pricelist(models.Model):
  worktype_id = models.AutoField(primary_key=True)
  worktype_name = models.CharField(max_length=100, blank=True, null=True)
  worktype_price = models.IntegerField(blank=True, null=True)

  class Meta:
    db_table = 'pricelist'


class Masters(models.Model):
  master_id = models.AutoField(primary_key=True)
  master_name = models.CharField(max_length=100, blank=True, null=True)

  class Meta:
    db_table = 'masters'


class Brands(models.Model):
  brand_id = models.AutoField(primary_key=True)
  brand_name = models.CharField(max_length=100, blank=True, null=True)

  class Meta:
    db_table = 'brands'


class Workshops(models.Model):
  workshop_id = models.AutoField(primary_key=True)
  workshop_address = models.CharField(max_length=100, blank=True, null=True)
  workshop_opentime = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
  workshop_closetime = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
  workshop_name = models.CharField(max_length=100, blank=True, null=True)

  class Meta:
    db_table = 'workshops'


class Masterlist(models.Model):
  masterlist_id = models.AutoField(primary_key=True)
  workshop = models.ForeignKey(Workshops, on_delete=models.CASCADE)
  master = models.ForeignKey(Masters, on_delete=models.CASCADE)

  class Meta:
    db_table = 'masterlist'


class Brandlist(models.Model):
  brandlist_id = models.AutoField(primary_key=True)
  workshop = models.ForeignKey(Workshops, on_delete=models.CASCADE)
  brand = models.ForeignKey(Brands, on_delete=models.CASCADE)

  class Meta:
    db_table = 'brandlist'


class Cars(models.Model):
  car_id = models.AutoField(primary_key=True)
  passport_number = models.CharField(max_length=100, blank=True, null=True)
  gov_number = models.CharField(max_length=100, blank=True, null=True)
  brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
  car_year = models.DateField()
  owner_name = models.CharField(max_length=100, blank=True, null=True)
  owner_address = models.CharField(max_length=100, blank=True, null=True)

  class Meta:
    db_table = 'cars'


class Works(models.Model):
  work_id = models.AutoField(primary_key=True)
  date_arrival = models.DateField(blank=True, null=True)
  date_done = models.DateField(blank=True, null=True)
  worktype = models.ForeignKey(Pricelist, on_delete=models.CASCADE, default=1)
  masterlist = models.ForeignKey(Masterlist, on_delete=models.CASCADE)

  class Meta:
    db_table = 'works'


class Documents(models.Model):
  document_id = models.AutoField(primary_key=True)
  car = models.ForeignKey(Cars, on_delete=models.CASCADE)

  class Meta:
    db_table = 'documents'


class Workslist(models.Model):
  row_id = models.AutoField(primary_key=True)
  document = models.ForeignKey(Documents, on_delete=models.CASCADE)
  work = models.ForeignKey(Works, on_delete=models.CASCADE)

  class Meta:
    db_table = 'workslist'