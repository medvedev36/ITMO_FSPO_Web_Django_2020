from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic import View

from .models import *
from django.views.generic.edit import CreateView, UpdateView
from .forms import *


def book_list(request):
    book = Book.objects.all()
    return render(request, "book/book_list.html", {"book": book})


def book_single(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, "book/book_single.html", {"book": book})


class DeleteBook(View):
    def get(self, request, pk):
        object = get_object_or_404(Book, id=pk)
        return render(request, "delete.html", context={"object": object})

    def post(self, request, pk):
        object = get_object_or_404(Book, id=pk)
        object.delete()
        return redirect("book_list")


class AddBook(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = "add.html"

    def form_valid(self, form):
        form.save()
        return redirect("book_list")


class UpdateBook(UpdateView):
    model = Book
    form_class = AddBookForm
    template_name = "add.html"

    def get_success_url(self):
        return reverse('book_list')


class AddAuthor(CreateView):
    model = Author
    form_class = AddAuthorForms
    template_name = "add.html"

    def form_valid(self, form):
        form.save()
        return redirect("author_list")


class UpdateAuthor(UpdateView):
    model = Author
    form_class = AddAuthorForms
    template_name = "add.html"

    def get_success_url(self):
        return reverse('author_list')


class ListAuthor(ListView):
    model = Author
    template_name = "author/list.html"


class DeleteAuthor(View):
    def get(self, request, pk):
        object = get_object_or_404(Author, id=pk)
        return render(request, "delete.html", context={"object": object})

    def post(self, request, pk):
        object = get_object_or_404(Author, id=pk)
        object.delete()
        return redirect("author_list")


class AddEdition(CreateView):
    model = Edition
    form_class = AddEditionForms
    template_name = "add.html/"

    def form_valid(self, form):
        form.save()
        return redirect("edition_list")


class UpdateEdition(UpdateView):
    model = Edition
    form_class = AddEditionForms
    template_name = "add.html"

    def get_success_url(self):
        return reverse('edition_list')


class ListEdition(ListView):
    model = Edition
    template_name = "edition/list.html"


class DeleteEdition(View):
    def get(self, request, pk):
        object = get_object_or_404(Edition, id=pk)
        return render(request, "delete.html", context={"object": object})

    def post(self, request, pk):
        object = get_object_or_404(Edition, id=pk)
        object.delete()
        return redirect("edition_list")


class AddCustomer(CreateView):
    model = Customer
    form_class = AddCustomerForms
    template_name = "add.html/"

    def form_valid(self, form):
        form.save()
        return redirect("customer_list")


class UpdateCustomer(UpdateView):
    model = Customer
    form_class = AddCustomerForms
    template_name = "add.html"

    def get_success_url(self):
        return reverse('customer_list')


class ListCustomer(ListView):
    model = Customer
    template_name = "customer/list.html"


class DeleteCustomer(View):
    def get(self, request, pk):
        object = get_object_or_404(Customer, id=pk)
        return render(request, "delete.html", context={"object": object})

    def post(self, request, pk):
        object = get_object_or_404(Customer, id=pk)
        object.delete()
        return redirect("customer_list")


class AddOrder(CreateView):
    model = Order
    form_class = AddOrderForms
    template_name = "add.html/"

    def form_valid(self, form):
        form.save()
        return redirect("order_list")


class UpdateOrder(UpdateView):
    model = Order
    form_class = AddOrderForms
    template_name = "add.html"

    def get_success_url(self):
        return reverse('order_list')


class ListOrder(ListView):
    model = Order
    template_name = "order/list.html"


class DeleteOrder(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, "delete.html", context={"object": order})

    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        order.delete()
        return redirect("order_list")
