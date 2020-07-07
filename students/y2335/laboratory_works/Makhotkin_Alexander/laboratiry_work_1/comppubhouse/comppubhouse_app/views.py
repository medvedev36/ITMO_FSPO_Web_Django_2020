import datetime

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth, messages
from django.utils.html import strip_tags

from .forms import *
from .models import *


# Create your views here.


def orders(request):
    customer_orders = Order.objects.filter(customer_id=request.user.id, bought=True).order_by('-date_order')

    for order in customer_orders:
        sum_price = 0
        sum_count = 0
        books_in_order = BooksInOrder.objects.filter(order=order).values('book')
        books = Book.objects.filter(isbn__in=books_in_order)
        order.books = books
        for book in books:
            try:
                book_in_order = BooksInOrder.objects.get(order_id=order, book_id=book.isbn)
                book.selected_count = book_in_order.count
                book.bought_price = book_in_order.price
                sum_price += book.selected_count * book.bought_price
                sum_count += book.selected_count
            except:
                book.selected_count = 0
        order.sum_price = sum_price
        order.sum_count = sum_count

    context = {
        'customer_orders': customer_orders,
    }
    return render(request, 'orders.html', context)


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            text = strip_tags(form.cleaned_data['text'])
            score = int(form.cleaned_data['score'])
            add_feedback(request, text, score)
            messages.success(request, 'Отзыв опубликован')

        return HttpResponseRedirect(request.path_info)

    form = FeedbackForm()
    form.fields['score'].initial = 10

    feedback_data = Feedback.objects.all().order_by('-date')

    context = {
        'form': form,
        'feedback_data': feedback_data,
    }
    return render(request, 'feedback.html', context)


def add_feedback(request, text, score):
    fb = Feedback()
    fb.customer_id = request.user.id
    fb.text = text
    fb.score = score
    fb.date = datetime.date.today()
    fb.save()
    return


def cart(request):
    if request.POST.get('btn_remove', None) is not None:
        remove_book(request.POST['isbn'], request)
        return HttpResponseRedirect(request.path_info)

    if request.POST.get('btn_edit', None) is not None:
        remove_book(request.POST['isbn'], request)
        status = add_book(request.POST['isbn'], int(request.POST['count']), request)
        if status == 'out':
            messages.error(request, "Книга закончилась на складе")
        elif status == 'less':
            messages.warning(request, "Изменено на меньше, так как отсутствует на складе")
        else:
            messages.success(request, "Количество успешно изменено")
        return HttpResponseRedirect(request.path_info)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.get(id=request.user.id)
            customer.address = strip_tags(form.cleaned_data['address'])
            customer.phone_number = form.cleaned_data['phone']
            customer.save()

            order = get_order_or_create(request)
            count_changes = update_books(order)
            if count_changes > 0:
                messages.warning(request, 'Количество доступных книг на складе изменилось, некоторые книги могут '
                                          'отсутствовать. Проверьте заказ и нажмите кнопку заказа повторно.')
                return HttpResponseRedirect(request.path_info)

            make_order(order)
            messages.success(request, 'Заказ успешно оформлен')
        return HttpResponseRedirect(request.path_info)

    form = OrderForm()
    customer = Customer.objects.get(id=request.user.id)
    form.fields['address'].initial = customer.address
    form.fields['phone'].initial = customer.phone_number

    order = get_order_or_create(request)
    books_in_order = BooksInOrder.objects.filter(order_id=order).values('book')
    books = Book.objects.filter(isbn__in=books_in_order)

    sum_price = 0
    sum_count = 0

    for book in books:
        try:
            book.selected_count = BooksInOrder.objects.get(order_id=order, book_id=book.isbn).count
            sum_price += book.selected_count * book.price
            sum_count += book.selected_count
        except:
            book.selected_count = None

    context = {
        'books': books,
        'sum_price': sum_price,
        'sum_count': sum_count,
        'form': form,
    }
    return render(request, 'cart.html', context)


def make_order(order):
    books_in_order = BooksInOrder.objects.filter(order_id=order)
    for book_in_order in books_in_order:
        book = Book.objects.get(isbn=book_in_order.book.isbn)
        book.count -= book_in_order.count
        book.save()
    order.bought = True
    order.date_order = datetime.datetime.now()
    order.save()
    return


def update_books(order):
    books_in_order = BooksInOrder.objects.filter(order_id=order)
    count_changes = 0
    for book in books_in_order:
        new_count = get_optimal_count(book.book.isbn, book.count)
        if book.count != new_count:
            count_changes += 1
    return count_changes


def catalog(request):
    if request.POST.get('btn_add', None) is not None:
        status = add_book(request.POST['isbn'], int(request.POST['count']), request)
        if status == 'out':
            messages.error(request, "Книга закончилась на складе")
        elif status == 'less':
            messages.warning(request, "Добавлено меньше, так как отсутствует на складе")
        else:
            messages.success(request, "Книга успешно добавлена")
        return HttpResponseRedirect(request.path_info)

    if request.POST.get('btn_remove', None) is not None:
        remove_book(request.POST['isbn'], request)
        return HttpResponseRedirect(request.path_info)

    books = Book.objects.all()

    if request.user.is_authenticated:
        order = get_order_or_create(request)
        books_in_order = BooksInOrder.objects.filter(order_id=order)
        for book in books:
            for bio in books_in_order:
                if book.isbn == bio.book_id:
                    book.selected_count = bio.count
            book_circ = Circulation.objects.filter(book=book).order_by('-date').first()
            book.circulation = book_circ
    context = {
        'books': books,
    }
    return render(request, 'catalog.html', context)


def get_order_or_create(request):
    try:
        order = Order.objects.get(customer_id=request.user.id, bought=False)
    except:
        order = Order()
        order.customer_id = request.user.id
        order.save()
    return order


def add_book(isbn, count, request):
    order = get_order_or_create(request)

    try:
        book_in_order = BooksInOrder.objects.get(book_id=isbn, order_id=order.id)
    except:
        book_in_order = BooksInOrder()
        book_in_order.book_id = isbn
        book_in_order.order = order
        book_in_order.price = Book.objects.get(isbn=isbn).price

    book_in_order.count = get_optimal_count(isbn, count)
    if book_in_order.count == 0:
        return 'out'
    else:
        book_in_order.save()
    if book_in_order.count != count:
        return 'less'
    return 'success'


def get_optimal_count(isbn, count):
    have_count = Book.objects.get(isbn=isbn).count
    if have_count < count:
        count = have_count
    return count


def remove_book(isbn, request):
    order = get_order_or_create(request)
    book_in_order = BooksInOrder.objects.get(order=order, book_id=isbn)
    if book_in_order is not None:
        book_in_order.delete()
    return


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                user = Customer.objects.create_user(
                    username=strip_tags(form.cleaned_data['username']),
                    email=strip_tags(form.cleaned_data['email']),
                    password=form.cleaned_data['password'],
                )
                user.first_name = strip_tags(form.cleaned_data['first_name'])
                user.last_name = strip_tags(form.cleaned_data['last_name'])
                user.save()
                auth.login(request, user)
                messages.success(request, "Вы успешно зарегистрировались")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Пароли не совпадают")
        else:
            messages.error(request, "Ошибка: не все поля введены")
        return HttpResponseRedirect(request.path_info)
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def edit_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            username = request.user.username
            password = form.cleaned_data['old_password']
            user_check = authenticate(username=username, password=password)
            if user_check is not None:
                if form.cleaned_data['new_password'] == form.cleaned_data['new_password2']:
                    user = Customer.objects.get(id=request.user.id)
                    user.set_password(form.cleaned_data['new_password'])
                    user.save()
                    messages.success(request, "Пароль успешно изменён")
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, "Пароли не совпадают")
            else:
                messages.error(request, "Введён неверный пароль")
            return HttpResponseRedirect(request.path_info)
    else:
        form = PasswordForm()
    return render(request, 'edit_password.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = Customer.objects.get(id=request.user.id)
            user.first_name = strip_tags(form.cleaned_data['first_name'])
            user.last_name = strip_tags(form.cleaned_data['last_name'])
            user.email = strip_tags(form.cleaned_data['email'])
            user.phone_number = form.cleaned_data['phone']
            user.address = strip_tags(form.cleaned_data['address'])
            user.save()
            messages.success(request, "Данные профиля сохранены")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, "Ошибка: не все поля введены")
    else:
        form = ProfileForm()
        user = Customer.objects.get(id=request.user.id)
        form.fields['first_name'].initial = user.first_name
        form.fields['last_name'].initial = user.last_name
        form.fields['email'].initial = user.email
        form.fields['phone'].initial = user.phone_number
        form.fields['address'].initial = user.address
    return render(request, 'edit_profile.html', {'form': form})


def main_page(request):
    state = login(request)
    if not state:
        return render(request, 'main_page.html')
    elif state == 'login':
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def login(request):
    btn_auth = request.POST.get('btn_auth', None)
    btn_deauth = request.POST.get('btn_deauth', None)
    if btn_auth is not None and request.user.is_authenticated == False:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
        else:
            messages.error(request, "Логин или пароль неверный!")
        return 'login'
    if btn_deauth is not None and request.user.is_authenticated == True:
        auth.logout(request)
        return 'logout'
    return False
