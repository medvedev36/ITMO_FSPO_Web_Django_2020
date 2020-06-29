from django.urls import path
from . import views
from .views import AllProducts, FlowerDetail, AllOrders , DeleteOrder
urlpatterns = [
    path('', AllProducts, name='flowers_list_url'),
    path('flower/<int:flower_id>/', FlowerDetail, name='flower_detail_url'),
    path('orders/', AllOrders, name='orders_list_url'),
    path('deleted/<int:id>/', DeleteOrder, name='deleted')

]