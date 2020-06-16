from django.urls import path
from Pract1 import views
urlpatterns = [
     path('user/<int:user_id>/', views.detail)
 ]