from django.shortcuts import render
from project_first_app.models import *
from django.shortcuts import get_object_or_404


def view_users(request, pk):
    user = get_object_or_404(Person, pk=pk) #Person.objects.get(2)

    context = {
        'user': user,
    }

    return render(request, 'main.html', context)


