from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Client.objects.create(user=instance)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return str(self.user)


class Customers(models.Model):
    passport = models.CharField(max_length=60)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    category_choice = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    category = models.CharField(max_length=1, choices=category_choice)
    position_choice = (
        (1, 'cock'),
        (2, 'waiter')
    )
    position = models.IntegerField(choices=position_choice)
    salary_cast = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def save(self, *args, **kwargs):
        if self.category == 'A':
            self.salary_cast = 30000
        elif self.category == 'B':
            self.salary_cast = 20000
        elif self.category == 'C':
            self.salary_cast = 10000

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Ingredient(models.Model):
    ingredient_code = models.IntegerField()
    ingredient_name = models.CharField(max_length=60)
    ingredient_price = models.IntegerField()

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.ingredient_name


class Dishes(models.Model):
    dish_code = models.IntegerField()
    dish_name = models.CharField(max_length=60)
    cook_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    price = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.dish_name

    def save(self, *args, **kwargs):
        total_price = 0
        try:
            for ingredient in Dishes.objects.get(dish_code=self.dish_code).ingredients.all():
                total_price += ingredient.ingredient_price

            self.price = total_price * 1.4
        except:
            pass
        super().save(*args, **kwargs)


class Purchase(models.Model):# склад
    purchase_code = models.IntegerField(unique=True)
    ingredient_code = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    volume_purchase = models.IntegerField()
    count_prod = models.IntegerField()
    product_stock = models.IntegerField()
    supplier = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'

    def __str__(self):
        return self.purchase_code


class Orders(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    date_order = models.DateField(auto_now_add=True)
    dishes = models.ManyToManyField(Dishes, blank=True)
    check = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.client} - {self.date_order}'


class Reservation(models.Model):
    table_reservation = models.ForeignKey('Table', on_delete=models.CASCADE, blank=True, null=True)
    time_choice = (
        ('13:00-14:00', '13:00-14:00'),
        ('14:00-15:00', '14:00-15:00'),
        ('15:00-16:00', '15:00-16:00'),
        ('16:00-17:00', '16:00-17:00'),
        ('17:00-18:00', '17:00-18:00'),
        ('18:00-19:00', '18:00-19:00'),
        ('20:00-21:00', '20:00-21:00'),
    )
    time = models.CharField(max_length=20, choices=time_choice)
    client = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

    def __str__(self):
        return f'{self.table_reservation} - {self.time}'


class Table(models.Model):
    table_number = models.IntegerField()
    # order_code = models.ForeignKey(Orders, on_delete=models.CASCADE)
    waiter_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    reservation_time = models.ManyToManyField(Reservation)

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def __str__(self):
        return str(self.table_number)


class Support(models.Model):
    email = models.EmailField(max_length=30)
    review = models.TextField()
