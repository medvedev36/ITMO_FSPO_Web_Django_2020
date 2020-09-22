from . import views

from django.urls import path

urlpatterns = [
    path('owners/<int:owner_id>/', views.detail)
]