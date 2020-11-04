from django.db import models


class Group(models.Model):
    number_group = models.CharField(max_length=10)
    number_of_student = models.IntegerField()


class Lecture(models.Model):
    TYPE_LEC = {
        ('Лекционный класс', 'Лекционный класс'),
        ('Лабораторный класс', 'Лабораторный класс'),
    }
    number_lecture = models.IntegerField()
    number_of_post = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_LEC)


class Subject(models.Model):
    name = models.CharField(max_length=50)


class Teacher(models.Model):
    name = models.CharField(max_length=50)


class Lesson(models.Model):
    TYPE_LES = {
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
    }
    number_group = models.CharField(max_length=10)
    number_lecture = models.IntegerField()
    teacher = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.CharField(max_length=20, choices=TYPE_LES)

# Create your models here.
