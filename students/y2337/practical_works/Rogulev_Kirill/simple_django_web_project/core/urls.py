from django.urls import path
from . import views

urlpatterns = [

    path('owner/<int:owner_id>/', views.owner),
    path('owner/list/', views.owner_list),
    path('owner/new/', views.owner_create),

    path('car/<int:car_id>/', views.car),
    path('car/list/', views.car_list.as_view()),
    path('car/new/', views.car_create.as_view()),
]
