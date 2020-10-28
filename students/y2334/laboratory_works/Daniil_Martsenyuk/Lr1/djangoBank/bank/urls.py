from django.urls import path
from bank.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name="home"),

    path('login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path('registration', registration_view, name='registration'),

    path('user_profile', user_profile_view, name='user_profile'),

    path('create_account', create_account, name='create_account'),
    path('user_account', user_account_view, name="user_account"),

    path('create_contract', create_contract_view, name="create_contract"),
    path('user_contract', user_contract_view, name="user_contract"),

    path('support', send_report, name="support"),
]
