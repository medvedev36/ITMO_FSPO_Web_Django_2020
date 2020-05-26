from django.contrib import admin
from django.urls import path, include
from Ivakhniuk_app import views
from .views import AutoList
from .views import AutoForm
urlpatterns = [

    path('app_date/', views.current_datetime),
    path('detail/<int:poll_id>/', views.detail),
    path('', views.list_view),
    path('Auto_list', AutoList.as_view()),
    path('add_user', views.create_view),
    path('add_auto', AutoForm.as_view()),

]