from django.urls import path
from . import views

urlpatterns = [
    path('owners/<int:owner_id>', views.ownerDetails),
    path('owners', views.allOwners),
    path('autos', views.AutoView.as_view()),
    path('owner/create', views.create_owner),
    path('auto/create', views.AutoCreate.as_view()),
]