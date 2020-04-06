from django.urls import path
from . import views
urlpatterns = [
    path('owner/<int:user_id>/', views.owner),

]