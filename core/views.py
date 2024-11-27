from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

from .models import Producto

# Create your views here.
def index(request):
    productos  = Producto.objects.all()
    paginator  = Paginator(productos, 6)
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


def contact(request):
    """
    SE DEBE REGISTRAR EN BDD EL CONTACTO Y ADICIONAR LOS CAMPOS AL FORMULARIO EN EL FRONT
    """
    if request.method == 'GET':
        return render(request, 'contact.html')
    else:
        nombres                  = request.POST['inputNombres']
        apellidos                = request.POST['inputApellidos']
        email_client             = request.POST['inputEmailFrom']
        mensaje                  = request.POST['inputMessage']
        correo                   = EmailMessage(
            subject='BIOCOLIBRISTORE - {} {} -> Lo envío: {}'.format(nombres, apellidos, email_client),
            body=mensaje,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.ADMIN_EMAIL],
        )
        try:
            envio = correo.send(fail_silently=False)
            if envio == 0:
                return render(request, 'contact.html', {'error':'¡Ups! No se puedo enviar el correo.'})
            else:
                return render(request, 'contact.html', {'mensaje':'¡El mensaje se ha enviado satisfactoriamente!'})
        except Exception as err:
            return render(request, 'contact.html', {'error':f'Ha ocurrido un error inseperado: {str(err)}'})
