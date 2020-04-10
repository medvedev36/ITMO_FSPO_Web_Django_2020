from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Possession, Auto
from django.http import HttpResponse

# Create your views here.
def index(request, fk):
    try: 
        content = {
            'user': User.objects.get(id=fk),
        }
    except User.DoesNotExist:
        return HttpResponse(status=404)
    cars = Auto.objects.filter(possession__owner=content['user'])
    content['cars'] = cars
    return render(request, 'core/base.html', content)
