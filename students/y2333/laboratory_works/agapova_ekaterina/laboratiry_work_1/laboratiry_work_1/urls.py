"""laboratiry_work_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from final_app import views
from django.urls import path, include

"""Регситрация REST urls"""
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'fabrics', views.FabricViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'deliveries', views.DeliveryViewSet)
router.register(r'sales', views.SaleViewSet)

"""Регистрация собственных view"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('store/', views.StoreList.as_view()),
    path('user/sale/', views.UserSales.as_view()),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^user/register', views.create_auth),
    url(r'^user/', views.UserData.as_view()),
]
