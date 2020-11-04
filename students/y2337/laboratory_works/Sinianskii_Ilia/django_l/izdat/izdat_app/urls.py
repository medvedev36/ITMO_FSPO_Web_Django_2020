from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('', views.book_list, name="book_list"),
    path('single/<int:pk>', views.book_single, name="book_single"),
    path("book/add_book/", views.AddBook.as_view(), name="add_book"),
    path("book/update/<int:pk>", views.UpdateBook.as_view(), name="book/update/"),
    path("book/delete/<int:pk>", views.DeleteBook.as_view(), name="book_delete"),

    path("author/add_author/", views.AddAuthor.as_view(), name="add_author"),
    path("author/update/<int:pk>", views.UpdateAuthor.as_view(), name="author/update/"),
    path('author/list/', views.ListAuthor.as_view(), name="author_list"),
    path("author/delete/<int:pk>", views.DeleteAuthor.as_view(), name="author_delete"),

    path("edition/add/", views.AddEdition.as_view(), name="add_edition"),
    path("edition/update/<int:pk>", views.UpdateEdition.as_view(), name="edition/update/"),
    path('edition/list/', views.ListEdition.as_view(), name="edition_list"),
    path("edition/delete/<int:pk>", views.DeleteEdition.as_view(), name="edition_delete"),

    path("customer/add/", views.AddCustomer.as_view(), name="add_customer"),
    path("customer/update/<int:pk>", views.UpdateCustomer.as_view(), name="customer/update/"),
    path('customer/list/', views.ListCustomer.as_view(), name="customer_list"),
    path("customer/delete/<int:pk>", views.DeleteCustomer.as_view(), name="customer_delete"),

    path("order/add/", views.AddOrder.as_view(), name="add_order"),
    path("order/update/<int:pk>", views.UpdateOrder.as_view(), name="order/update/"),
    path('order/list/', views.ListOrder.as_view(), name="order_list"),
    path("order/delete/<int:pk>", views.DeleteOrder.as_view(), name="order_delete"),

]