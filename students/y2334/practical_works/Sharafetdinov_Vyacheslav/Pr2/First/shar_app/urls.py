from django.urls import path

from .import views

urlpatterns = [
    path('', views.default),
    path('owner/<int:owner_id>/', views.OwnerInfo),
    path('owners/', views.list_owners),
    path('autos/', views.list_autos.as_view()),
    path('owner_add/', views.form_owner),
    path('auto_add/', views.form_auto.as_view()),
]