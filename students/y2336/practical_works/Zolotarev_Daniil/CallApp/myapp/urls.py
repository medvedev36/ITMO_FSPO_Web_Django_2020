from django.urls import path
from .views import *

urlpatterns = [
    # path('myapp/', post_list),
    path('users_list/', users_list, name='users_list_url'),
    path('rates_list/', rates_list, name='rates_list_url'),
    path('calls_list/', calls_list, name='calls_list_url'),
    path('cashes_list/', cashes_list, name='cashes_list_url'),
    path('users_calls_list/', users_calls_list, name='users_calls_list_url'),
    path('account/create', account_create, name='account_create_url'),
    path('account/<slug:login>/main/', certain_user, name='certain_user_url'),
    path('autentification/', autentification, name='autentification'),
    path('account/<slug:login>/rates/', certain_user_rates, name='certain_user_rates_url'),
    path('account/<slug:login>/calls/', certain_user_calls, name='certain_user_calls_url'),
    path('account/<slug:login>/information/', certain_user_information, name='certain_user_information_url'),
    path('account/<slug:login>/user_binding/', certain_user_binding, name='certain_user_binding_url'),
    path('account/<slug:login>/cash/', certain_user_cash, name='certain_user_cash_url'),
    path('account/<slug:login>/cash_pay_for_calls/', pay_for_calls, name='pay_for_calls_url'),
]
