from django.contrib import admin
from django.urls import path, include

from app.views import *

urlpatterns = [
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/logout/', logout, name="logout_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', reader_all, name="home_url"),
    path('book_add', book_add, name="book_add_url"),
    path('reader_add', reader_add, name="reader_add_url"),
    path('reader', reader_all, name="reader_all_url"),
    path('reader/<int:reader_id>/', reader, name="reader_url"),
    path('reader/<int:reader_id>/card_add/', card_add, name="card_add_url")
]