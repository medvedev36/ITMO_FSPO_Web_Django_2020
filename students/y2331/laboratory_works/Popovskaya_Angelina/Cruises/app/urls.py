from django.urls import path, include
from django.urls import reverse
from .views import *


urlpatterns = [
    path('base', base, name='base_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/<int:user_id>/', account, name='account_url'),
    path('selling/<int:excursion_id>/<int:user_id>/', selling, name='selling_url'),
    path('excursion/<int:excursion_id>/', excursion, name='excursion_url'),
    path('singup', MyRegisterFormView.as_view(), name='signup_url'),
    path('excursion_add', excursion_add, name='excursion_add_url'),
    path('excursion_delete/<int:excursion_id>/', excursion_delete, name='excursion_delete_url'),
]