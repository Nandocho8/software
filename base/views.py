from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base/index.html')


class Ofertas(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base/ofertas.html')


def prov(request):
    return render(request, 'base/proveedores.html')


def serv(request):
    return render(request, 'base/servicios.html')
