from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.authorsList),
    path('authors/<int:author_id>', views.authorDetails),
    path('books', views.booksList),
    path('books/<int:book_id>', views.bookDetails),
    path('order', views.createOrder),
    path('', views.mainPage),
]