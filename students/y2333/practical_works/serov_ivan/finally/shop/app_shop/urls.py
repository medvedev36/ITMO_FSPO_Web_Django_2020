from django.urls import path, include
from django.urls import reverse
from .views import *


urlpatterns = [
    path('base', base, name='base_url'),
    path('search', search, name='search_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/<int:user_id>/', account, name='account_url'),
    path('selling/<int:user_id>/<int:cassette_id>/', selling, name='selling_url'),
    path('sort/<str:theme>/', sort, name='sort_url'),
    path('singup', signup, name='signup_url'),
    path('cassette_add', cassette_add, name='cassette_add_url'),
    path('cassette_delete/<int:cassette_id>/', cassette_delete, name='cassette_delete_url'),
    path('show_for_delete', show_for_delete, name='show_for_delete_url'),
]