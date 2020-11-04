from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_us, name='about-us'),
    path('car/', views.CarListView.as_view(), name='car-list'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('car_class/', views.CarClassListView.as_view(), name='carclass-list'),
    path('car_class/<int:pk>/', views.CarClassDetailView.as_view(), name='carclass-detail'),
    path('license/', views.LicenseCreateView.as_view(), name='license'),
    path('car/new/', views.CarCreateView.as_view(), name='car-new'),

    path('car/<int:pk>/rent/', views.RentCreateView.as_view(), name='rent-new'),

    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]
