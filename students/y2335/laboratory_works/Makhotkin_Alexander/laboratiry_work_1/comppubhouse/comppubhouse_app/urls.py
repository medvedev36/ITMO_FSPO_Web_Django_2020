from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('profile/edit', login_required(edit_profile), name='edit_profile'),
    path('profile/password', login_required(edit_password), name='edit_password'),
    path('registration', registration, name='registration'),
    path('catalog', catalog, name='catalog'),
    path('cart', login_required(cart), name='cart'),
    path('feedback', feedback, name='feedback'),
    path('orders', login_required(orders), name='orders'),
]