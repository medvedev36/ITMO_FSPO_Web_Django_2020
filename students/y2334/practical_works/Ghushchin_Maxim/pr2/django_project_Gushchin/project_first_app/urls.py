from django.urls import path, include
from project_first_app.views import *

urlpatterns = [
    path('user/<int:pk>', view_users, name='view_users'),
    path('users', all_users),
    path('cars', Cars.as_view(), name='cars'),
    path('create_user', create_person),
    path('create_cars', AutosCreate.as_view()),
]
