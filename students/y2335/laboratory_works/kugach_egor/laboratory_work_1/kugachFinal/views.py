from django.shortcuts import render

# Create your views here.
from .models import Author, Book, Category, Orders, Edition
from .forms import OrderForm


def mainPage(request):
    return render(request, 'mainPage.html')


def booksList(request):
    b = Book.objects.all()
    return render(request, 'allBooksList.html', {'books': b})


def authorsList(request):
    a = Author.objects.all()
    return render(request, 'allAuthorsList.html', {'authors': a})


def bookDetails(request, book_id):
    b = Book.objects.get(pk=book_id)
    a = b.authors.all()
    return render(request, 'bookDetails.html', {'book': b, 'authors': a})


def authorDetails(request, author_id):
    a = Author.objects.get(pk=author_id)
    b = a.book_set.all()
    return render(request, 'authorDetails.html', {'author': a, 'books': b})


def createOrder(request):
    context = {}
    form = OrderForm(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'OrderCreation.html', context)
