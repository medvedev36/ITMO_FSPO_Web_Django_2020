from django.urls import path
from .import views
from .views import AutoCreate, AutoList
urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('ownerview/', views.ownerview),
    path('autoview/', views.autoview),
    path('create_owner/', views.create_owner),
    path('autolist/', AutoList.as_view()),
    path('create_auto/', AutoCreate.as_view()),
    path('auto/<int:auto_id>/', views.auto_detail),
]
