from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
import datetime

from django.views.generic.edit import CreateView
from django.http import Http404
from django.shortcuts import render
from .models import CD, SellArrival, Album, CdHasAlbum, Track
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CDForm, AlbumCDForm, ArrivalForm, TrackForm, AlbumForm
from django.views.generic.edit import CreateView
from django.contrib.admin.views.decorators import staff_member_required


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/accounts/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    @login_required(login_url='/accounts/login/')
    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


@login_required(login_url='/accounts/login/')
def cd_list(request):
   context = {}
   context["dataset"] = CD.objects.raw('select Salon_app_cd.id, Salon_app_cd.price,  Salon_app_cd.name, Salon_app_company_maker.name, sum(amount) - (SELECT count(op_code) from Salon_app_sellarrival where op_code="S" and Salon_app_cd.id=CD_id_id GROUP by CD_id_id)  as cou from Salon_app_cd, Salon_app_company_maker, Salon_app_SellArrival where op_code = "A" and Salon_app_cd.id = Salon_app_sellarrival.CD_id_id group by Salon_app_SellArrival.CD_id_id')
   return render(request, "cd_page.html", context, )



@staff_member_required(login_url='/accounts/login/')
def sell_list(request):
    context = {}
    context["dataset"] = SellArrival.objects.filter(op_code="S")
    return render(request, "sell_list.html", context)


@login_required(login_url='/accounts/login/')
def topchart(request):
    context = {}
    context["dataset"] = CD.objects.raw('SELECT DISTINCT performer, Salon_app_album.id, album_name, genre, (select sum(tmp) from (SELECT count(CD_id_id) as tmp from Salon_app_sellarrival, Salon_app_cd where CD_id_id = Salon_app_cd.id) as tmp) as sm from Salon_app_CD, Salon_app_SellArrival, Salon_app_album, Salon_app_cdhasalbum, Salon_app_track where Salon_app_album.id = Salon_app_cdhasalbum.Album_id_id and Salon_app_cdhasalbum.CD_id_id = Salon_app_cd.id and Salon_app_cd.id = Salon_app_sellarrival.CD_id_id and Salon_app_album.id = Salon_app_track.album_id_id and op_code = "S" GROUP by (SELECT count(CD_id_id) from Salon_app_sellarrival where CD_id_id = Salon_app_cd.id) order by (SELECT count(CD_id_id) from Salon_app_sellarrival where CD_id_id = Salon_app_cd.id) desc ;')
    return render(request, "topchart.html", context)


@login_required(login_url='/accounts/login/')
def buysucc(request, pollid):
    sa=CD.objects.get(pk = pollid)
    if (request.method == "POST"):
        sa1 = SellArrival()
        sa1.price = sa.price
        sa1.op_date = datetime.datetime.now()
        sa1.amount = 0
        sa1.op_code = "S"
        sa1.supplier = sa.company_id.name
        sa1.CD_id_id = sa.id
        sa1.save()
        return render(request, "check2.html", {'poll': sa1})
    return render(request, "check.html", {'poll': sa})


@login_required(login_url='/accounts/login/')
def cdinfo(request, pollid):
    context = {}
    cha = CdHasAlbum()
    cd = CD()
    context["dataset"] = Track.objects.select_related().filter(album_id__cdhasalbum__CD_id = pollid)
    return render(request, "cdinfo.html", context)


@login_required(login_url='/accounts/login/')
def arr_list(request):
    context = {}
    context["dataset"] = SellArrival.objects.filter(op_code="A")
    return render(request, "arrival_list.html", context)


@staff_member_required(login_url='/accounts/login/')
def create_cdview(request):
    context = {}
    form = CDForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Salon_app/succ')
    else:
        context['form'] = form
        return render(request, "cd_form.html", context)


@staff_member_required(login_url='/accounts/login/')
def create_cdalbumview(request):
    context = {}
    form = AlbumCDForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Salon_app/succ')
    else:
        context['form'] = form
        return render(request, "alcd_form.html", context)


@staff_member_required(login_url='/accounts/login/')
def create_arrview(request):
    context = {}
    form = ArrivalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Salon_app/succ')
    else:
        context['form'] = form
        return render(request, "arr_form.html", context)


@staff_member_required(login_url='/accounts/login/')
def track_list(request):
    context = {}
    context["dataset"] = Track.objects.all()
    return render(request, "track_list.html", context)


@staff_member_required(login_url='/accounts/login/')
def create_albumview(request):
    context = {}
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Salon_app/succ')
    else:
        context['form'] = form
        return render(request, "album_form.html", context)


@staff_member_required(login_url='/accounts/login/')
def create_trackview(request):
    context = {}
    form = TrackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Salon_app/succ')
    else:
        context['form'] = form
        return render(request, "track_form.html", context)
