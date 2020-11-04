from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_detail),
    path('owner/list/', views.owner_list),
    path('owner/add/', views.owner_add),

    path('car/<int:car_id>/', views.car_detail),
    path('car/list/', views.CarList.as_view()),
    path('car/add/', views.AddCar.as_view()),

    # path('', views.list_view),
    # path('', GeeksList.as_view()),
    # path('', views.create_view),
    path('', views.GeeksCreate.as_view()),

]
