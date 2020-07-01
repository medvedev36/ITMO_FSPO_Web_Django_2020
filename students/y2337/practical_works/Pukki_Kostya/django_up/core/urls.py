from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner),
    path('owner/list/', views.ownerList),
    path('owner/new/', views.ownerCreate),

    path('car/<int:car_id>/', views.car),
    path('car/list/', views.CarList.as_view()),
    path('car/new/', views.CarCreate.as_view()),
]