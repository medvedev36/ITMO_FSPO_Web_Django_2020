from django.http import Http404
from django.shortcuts import render
from .models import User


def owner(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'owner.html', {'user': user})
