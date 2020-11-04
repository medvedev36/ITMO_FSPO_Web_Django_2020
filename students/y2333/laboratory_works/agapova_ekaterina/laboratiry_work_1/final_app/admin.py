from django.contrib import admin
from final_app.models import Product, Delivery, Fabric, Sale, User

"""Регистрация моделей для админки django"""
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(Fabric)
admin.site.register(Sale)

