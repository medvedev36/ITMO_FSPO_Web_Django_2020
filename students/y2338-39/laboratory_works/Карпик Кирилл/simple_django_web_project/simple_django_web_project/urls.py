"""simple_django_web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from autoshow.views import index, login_page, signup_page, logout_page, autoshow_page, order_page, message_page

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', index),
  path('login', login_page, name="login"),
  path('signup', signup_page, name="signup"),
  path("logout", logout_page, name="logout"),
  path("autoshow/<int:slug>/", autoshow_page, name="autoshow"),
  path("order/<int:slug>/", order_page, name="order"),
  path("ordered", message_page, name="ordered")
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
