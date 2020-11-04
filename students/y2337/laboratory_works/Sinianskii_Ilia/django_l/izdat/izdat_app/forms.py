from django import forms
from .models import *


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "category_code",
            "number_of_pages",
            "year_of_publication",
            "isbn_kode",
            "author_has_book",
            "price"
        ]


class AddAuthorForms(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "name",
            "surname",
        ]


class AddEditionForms(forms.ModelForm):
    class Meta:
        model = Edition
        fields = [
            "numbers_of_copies",
            "date",
            "price",
            "book_id",
        ]


class AddCustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "name",
            "surname",
            "address",
            "phone_num",
        ]


class AddOrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "date",
            "id_customer",
            "Book_has_Order",
        ]