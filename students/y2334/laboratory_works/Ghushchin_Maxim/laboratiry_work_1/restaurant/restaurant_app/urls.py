from django.urls import path
from restaurant_app.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main_page, name='main_page'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registration/', registration, name='registration'),
    path('tables/', view_tables, name='tables'),
    path('operation_with_reservation/<int:pk>/', operation_with_reservation, name='operation_with_reservation'),
    path('client_order/', client_order, name='client_order'),
    path('client_help/', client_help, name='client_help'),
    # path('client_form', client_form, name='client_form')
    path('menu/', view_menu, name='view_menu'),
    path('order/<int:pk>', add_order, name='add_order'),
    path('remove_order/<int:pk>', remove_order, name='remove_order'),
    path('cart/', view_cart, name='view_cart'),
    path('send_review/', send_review, name='send_review'),
    path('ty/', view_ty, name='view_ty'),
    path('close_order/', close_order, name='close_order'),
    path('confirmed_order/', confirmed_order, name='confirmed_order'),
    path('cancel_order/', cancel_order, name='cancel_order'),

]
