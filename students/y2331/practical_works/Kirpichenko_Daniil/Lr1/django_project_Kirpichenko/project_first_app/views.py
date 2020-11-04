from django.shortcuts import render
from .models import Owner
from django.http import Http404


# Create your views here.
def detail(request, poll_id):
    try:
        p = Owner.objects.get(pk=poll_id)
    except Owner.DoesNotExists:
        raise Http404("Poll does not exists")
    return render(request, 'project_first_app/owner.html', {'poll_id': p})
