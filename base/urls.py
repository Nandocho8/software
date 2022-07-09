"""larrain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import Index, Ofertas, prov, serv
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('ofertas/', login_required(Ofertas.as_view()), name='ofertas'),
    path('prov_exclusivos/', login_required(prov), name='prov'),
    path('detalle/', login_required(serv), name='servicio'),

]
