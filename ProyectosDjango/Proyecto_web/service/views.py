from django.shortcuts import render

from service.models import Service
# Create your views here.


def service(request): 
    service=Service.objects.all()
    return render(request, 'service.html', {'service':service})