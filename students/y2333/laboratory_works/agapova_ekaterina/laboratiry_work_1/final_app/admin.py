from django.contrib import admin
from final_app.models import Product, Delivery, Fabric, Sale, User

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(Fabric)
admin.site.register(Sale)

