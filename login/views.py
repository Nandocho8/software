from django.shortcuts import render, redirect
from .forms import CustomUser, FormDatosUser
from .util import *
from django.contrib.auth import authenticate, login
from django.http import QueryDict
# Create your views here.
from django.contrib import messages


def registro(request):
    data = {
        'form': CustomUser()
    }

    if request.method == 'POST':
        passw = password(10)
        csrfmiddlewaretoken = request.POST['csrfmiddlewaretoken']
        print(request.POST)
        username = request.POST['username']
        # name = request.POST['names']
        req = QueryDict(mutable=True)

        req.appendlist('csrfmiddlewaretoken', csrfmiddlewaretoken)
        req.appendlist('username', username)
        req.appendlist('password1', passw)
        req.appendlist('password2', passw)
        # ['csrfmiddlewaretoken', 'username', 'password1', 'password2'], mutable=True)
        # req.update({'csrfmiddlewaretoken': csrfmiddlewaretoken})
        print(req)

        form = CustomUser(data=req)
        if form.is_valid():
            form.save()
            mail(passw, username)
            user = authenticate(
                username=form.cleaned_data["username"], password=passw)
            messages.success(
                request, "Creado Correctamente, Inicio de sesión automatica te hemos enviado a tu correo la contraseña de acceso")
            login(request, user)
        else:
            messages.error(request, "El usuario ya esta creado")
        return redirect(to='index')
    return render(request, 'registration/registrate.html', data)


def datos(request):
    data = {
        'form': FormDatosUser()
    }
    if request.method == 'POST':
        formu = FormDatosUser(data=request.POST)
        if formu.is_valid():
            formu.save()
            return redirect(to='index')
        else:
            data['form'] = formu
            return render(request, 'registration/datos.html', data)
    else:
        return render(request, 'registration/datos.html', data)
