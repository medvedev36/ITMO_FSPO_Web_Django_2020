from django.urls import path, include
from .views import *



urlpatterns = [
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/logout/', logout, name="logout_url"),
    path('top', top, name="top_url"),
    path('disc', disc, name="disc_url"),
    path('disc_add', disc_add, name="disc_add_url"),
    path('disc_delete/<int:disc_id>', disc_delete, name="disc_delete_url"),
    path('disc_edit/<int:disc_id>', disc_edit, name="disc_edit_url"),
    path('sing_add', sing_add, name="sing_add_url"),
    path('singer_add', singer_add, name="singer_add_url"),
    path('singer', singer, name="singer_url"),
    path('sing', sing, name="sing_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('buy', buy, name="buy_url"),
    path('info_sing/<slug:disc_name>', info_sing, name="info_sing_url"),
]