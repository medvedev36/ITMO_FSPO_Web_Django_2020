from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import random
import datetime as dt

from .models import Workshops, Pricelist, Brandlist, Brands, Cars, Documents, Workslist, Works, Masterlist

# Create your views here.

colors = ["#17e6b3", "#17e6b3", "#23c8ab", "#df6877", "#fdccce", "#fdccce", "#de65aa", "#de65aa", "#b0a4d5", "#78d2e7", "#aafd99", "#fe8259"]

class dotdict(dict):
  """dot.notation access to dictionary attributes"""
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__

def index(request):
  if request.user.is_authenticated:
    username = request.user.username
    authenticated = True
  else:
    username = ""
    authenticated = False

  data = Workshops.objects.all()
  for i in range(len(data)):
    data[i].color = random.choice(colors)
    data[i].isopen = (data[i].workshop_opentime < dt.datetime.now().time() < data[i].workshop_closetime)

  print(data)

  return render(request, "index.html", {"authenticated": authenticated, "username": username, "data": data})

def message_page(request):
  if request.method == "POST":
    if request.user.is_authenticated:
      username = request.user.username
      authenticated = True
    else:
      username = ""
      authenticated = False

    print(request.POST)
    slug = int(request.POST.get("slug_id"))
    # data = dotdict({})
    workshop = Workshops.objects.get(workshop_id=slug)
    pricelist = Pricelist.objects.all()
    brands = [Brands.objects.get(brand_id=brand.brand_id) for brand in Brandlist.objects.filter(workshop_id=slug)]
    success = True
    brand_id = int(request.POST.get("brand_id"))
    passport = request.POST.get("passport")
    gov_number = request.POST.get("gov_number")
    car_year = request.POST.get("car_year")
    owner_name = request.POST.get("owner_name")
    address = request.POST.get("address")
    selected_works = request.POST.getlist("works")

    print(selected_works, selected_works is None)
    if selected_works is None:
      success = False
      message = "Выберете тип работы"
    else:
      car = Cars.objects.filter(passport_number=passport, gov_number=gov_number, owner_name=owner_name, owner_address=address)

      print("check if i need to create a car")
      if car.exists():
        c = car[0]
      else:
        c = Cars.objects.create(passport_number=passport, gov_number=gov_number, brand_id=brand_id, car_year=(car_year+'-01-01'), owner_name=owner_name, owner_address=address)

      print("making doc...")
      d = Documents.objects.create(car=c)

      print("making temp date...")
      date_prev = dt.datetime.now().date()
      print("making temp available_masters...")
      available_masters = Masterlist.objects.filter(workshop=workshop)
      print("looping")

      print("You chose: ")
      for worktype_id in selected_works:
        date_start = date_prev + dt.timedelta(days=(random.choice(range(7))))
        date_prev = date_start + dt.timedelta(days=(random.choice(range(30, 300))))
        print(worktype_id, int(worktype_id), '-', Pricelist.objects.get(worktype_id=(int(worktype_id))).worktype_name)
        wo = Works.objects.create(date_arrival=(str(date_start)), date_done=(str(date_prev)), worktype=(Pricelist.objects.get(worktype_id=(int(worktype_id)))), masterlist=(random.choice(available_masters)))
        wt = Workslist.objects.create(document=d, work=wo)

    if success:
      message = "Заказ успешно сделан"
      return render(request, "order.html", {"authenticated": authenticated, "username": username, "data": {"workshop": workshop, "pricelist": pricelist, "brands": brands, "success": success}, "message": message})
    else:
      error = True
      return render(request, "order.html", {"authenticated": authenticated, "username": username, "data": {"workshop": workshop, "pricelist": pricelist, "brands": brands, "success": success, "error": error}, "message": message})
  else:
    return redirect("/")

def order_page(request, slug):
  if request.user.is_authenticated:
    username = request.user.username
    authenticated = True
  else:
    username = ""
    authenticated = False

  data = dotdict({})
  data.workshop = Workshops.objects.get(workshop_id=slug)
  data.pricelist = Pricelist.objects.all()
  data.brands = [Brands.objects.get(brand_id=brand.brand_id) for brand in Brandlist.objects.filter(workshop_id=slug)]

  return render(request, "order.html", {"authenticated": authenticated, "username": username, "data": data})

def autoshow_page(request, slug):
  if request.user.is_authenticated:
    username = request.user.username
    authenticated = True
  else:
    username = ""
    authenticated = False

  data = Workshops.objects.get(workshop_id=slug)
  data.color = random.choice(colors)
  data.isopen = (data.workshop_opentime < dt.datetime.now().time() < data.workshop_closetime)

  return render(request, "autoshow.html", {"authenticated": authenticated, "username": username, "data": data})

def logout_page(request):
  logout(request)
  return redirect("/")

def login_page(request):

  if request.user.is_authenticated:
    return redirect("/")
  elif request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    print("You got this user", user)
    if user is not None:
      login(request, user)
      return redirect("/")

  return render(request, "registration/login.html", {})

def signup_page(request):

  if request.user.is_authenticated:
    return redirect("/")
  elif request.method == "POST":
    username = request.POST.get("username")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    password = request.POST.get("password")
    email = request.POST.get("email")

    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    user.save()
    return redirect("/")

  return render(request, "registration/signup.html", {})

# def pricelist_view(request):
#   pricelist = Pricelist.objects.all();
#   return render(request, "prices/index.html", {'pricelist': pricelist})