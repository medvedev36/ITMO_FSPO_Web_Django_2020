from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('brand/', BrandListView.as_view(), name='brand-list'),
    path('brand/new/', BrandCreateView.as_view(), name='brand-new'),
    path('brand/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-new'),
    path('purchase/<int:instock>/', buy_product, name='purchase-new'),
    path('store/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),

    path('login/', my_login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('logout/', my_logout, name='logout'),
]

