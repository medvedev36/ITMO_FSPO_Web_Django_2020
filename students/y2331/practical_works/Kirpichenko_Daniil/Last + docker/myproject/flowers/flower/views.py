from django.shortcuts import render
from .models import Products,Orders,OrderInformation,Employee,Clients
from .forms import OrderForm
from django.db.models import Q,Min,Max
from django.db import connection
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
import datetime

# Create your views here.


def AllProducts(request):
    search = request.GET.get('search', '')
    if search:
        products = Products.objects.filter(product_name__icontains=search)
    else:
        products = Products.objects.filter(~Q(product_count=0))
    return render(request, 'flower/products_list.html', context={'flowers': products})


def FlowerDetail(request, flower_id):
    flower = Products.objects.get(product_id=flower_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = OrderForm(request.POST)
            count = form['Count'].value()
            if int(count) > flower.product_count:
                return render(request, 'flower/message_about_login.html', context={'msg': 'Not enough flowers'})

            flower.product_count = (flower.product_count - int(count))
            flower.save()

            form = form.save(commit=False)
            form.user = request.user
            form.save()

            buf = Employee.objects.all().aggregate(Min('employee_orders'))
            buf1 = Clients.objects.all().aggregate(Max('client_id'))
            empl = Employee.objects.get(employee_orders= buf['employee_orders__min'])
            order = Orders(
                order_client_id = Clients.objects.get(client_id = buf1['client_id__max']),
                order_employee_id = empl,
                order_date = datetime.datetime.now()
            )
            order.save()

            empl.employee_orders += 1
            empl.save()

            orderInf = OrderInformation(
                order_id=Orders.objects.get(order_id = order.order_id),
                product_id = Products.objects.get(product_id = flower_id),
                order_product_count = int(count)
            )
            orderInf.save()

            return render(request, 'flower/succes.html', context={'msg': 'Your purchase cost :' + str((int(count) * flower.product_cost))})

        else:
            form = OrderForm()
            return render(request, 'flower/flower_detail.html', context={'form': form})
    else:
        return render(request, 'flower/message_about_login.html', context={'msg': 'You must be logged in'})


def AllOrders(request):
    orders = {}

    orders["orders"] = OrderInformation.objects.raw('select order_date ,flower_orderinformation.id as id,product_name, flower_orderinformation.order_product_count as count, employee_first_name,employee_last_name, client_first_name,client_last_name from flower_orderinformation,flower_employee,flower_clients,flower_products,flower_orders where flower_orderinformation.order_id_id = flower_orders.order_id AND flower_orders.order_client_id_id = flower_clients.client_id AND flower_orders.order_employee_id_id = flower_employee.employee_id AND flower_orderinformation.product_id_id = flower_products.product_id')
    return render(request, 'flower/orders_list.html', orders)


def DeleteOrder(request,id):
    govno = OrderInformation.objects.get(pk=id).delete()
    return render(request, 'flower/succes.html', context={'msg': "Object deleted His id was: " + str(id)})