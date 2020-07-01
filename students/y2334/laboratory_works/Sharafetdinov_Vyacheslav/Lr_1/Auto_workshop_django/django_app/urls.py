from django.urls import path
from .views import *

urlpatterns = [
    path('workshops_brands/', Workshops_list),
    path('owner_registration/', Owner_registration),
    path('owner_autos_list/', Onwer_autos_list),
    path('owner_auto_add/', Owner_auto_add),
    path('owner_auto_edit/<str:pk>/', Owner_auto_edit),
    path('owner_auto_remove/<str:pk>/', Owner_auto_remove),
    path('owner_applications_list/', Owner_applications_list),
    path('workshops_for_application_list/', Workshops_for_application_list),
    path('owner_application_add/', Owner_application_add),
    path('owner_application_remove/<str:pk>/', Owner_application_remove),
]