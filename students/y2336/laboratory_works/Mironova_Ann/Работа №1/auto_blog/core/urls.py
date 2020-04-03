from . import views
from django.urls import path


urlpatterns = [
    path('owner/<int:fk>', views.index)
]
