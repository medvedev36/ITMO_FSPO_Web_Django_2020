from django.shortcuts import render

# Create your views here.
from django.http import Http404
from .models import User


def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'owner.html', {'User': user})
