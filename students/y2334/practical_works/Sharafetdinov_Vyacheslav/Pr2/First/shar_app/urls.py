from django.urls import path

from .import views
from .views import list_autos

urlpatterns = [
    path('',views.default),
    path('owner/<int:owner_id>/',views.OwnerInfo),
    path('owners/',views.list_owners),
    path('autos/',list_autos.as_view()),
]