from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Car_owner
def owner(request,car_owner_id):
        try:
                car_owner = Car_owner.objects.get(pk=car_owner_id)
        except Car_owner.DoesNotExist:
                raise Http404("Owner does not exist")
        return render(request, 'owner.html', {'carowner': car_owner})
