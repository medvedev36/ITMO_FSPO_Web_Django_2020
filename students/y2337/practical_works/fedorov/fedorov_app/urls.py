from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('owners/<int:id>', details),
    path('car/list/', CarList.as_view()),
    path('owner/<int:owner_id>/', details),
    path('owner/list/', owner_list),
    path('car/create/', CarCreate.as_view()),
    path('owner/create', owner_create)
]
