from django.http import Http404
from django.shortcuts import render
from .models import User
from .models import Car
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import UserForm


def owner(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'project_first_app/owner.html', {'user': user})


def list_user(request):
    context = {}
    context["dataset"] = User.objects.all()
    return render(request, "project_first_app/list_user.html", context)


class CarList(ListView):
    model = Car


# def create_view(request):
#     context = {}
#
#     form = UserForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#     context['form'] = form
#     return render(request, "project_first_app/create_view.html", context)
def create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'project_first_app/create_view.html', {'form': form})


class CarCreate(CreateView):
    model = Car
    fields = ['mark', 'model']
