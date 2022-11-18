from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    paginator = Paginator(productos, 6)
    num_pagina = request.GET.get('page')
    paginacion = paginator.get_page(num_pagina)
    return render(request, 'index.html', {'productos':productos, 'paginacion':paginacion})


def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'singin.html', {'error':'¡Ups! Revisa tus credenciales.'})
        else:
            login(request, user)
            return redirect('index')


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html')
    else:
        username  = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return render(request, 'singup.html', {'error':'¡Ups! Revisa tu usuario o contraseña de nuevo.'})
        else:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'singup.html', {'error':'El usuario ya existe.'})


def singout(request):
    logout(request)
    return redirect('index')