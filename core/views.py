from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

from .models import Producto, Contacto

# Create your views here.
def index(request):
    productos  = Producto.objects.all()
    paginator  = Paginator(productos, 6)
    num_pagina = request.GET.get('page')
    paginacion = paginator.get_page(num_pagina)

    return render(request, 'index.html', {
        'productos':productos,
        'paginacion':paginacion
    })


def singin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'singin.html', {
                'error':'¡Ups! Revisa tus credenciales.'
            })
        else:
            login(request, user)
            return redirect('index')
    
    return render(request, 'singin.html')


def singup(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'singup.html', {
                'error':'¡Ups! Revisa tu usuario o contraseña de nuevo.'
            })
        else:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'error':'El usuario ya existe.'
                })
    
    return render(request, 'singup.html')


def singout(request):
    logout(request)
    return redirect('index')


def contact(request):
    if request.method == 'POST':
        name, last_name, email, message, subject, correo = __capture_data_email(request)
        try:
            envio = correo.send(fail_silently=False)
            if envio == 0:
                return render(request, 'contact.html', {
                    'error':'¡Ups! No se puedo enviar el correo.'
                })
            else:
                __save_contact(name, last_name, email, message, subject)
                return render(request, 'contact.html', {
                    'mensaje':'¡El mensaje se ha enviado satisfactoriamente!'
                })
        except Exception as err:
            return render(request, 'contact.html', {
                'error':f'Ha ocurrido un error inseperado: {str(err)}'
            })
    
    return render(request, 'contact.html')


def __capture_data_email(request):
    nombres                  = request.POST['inputNombres']
    apellidos                = request.POST['inputApellidos']
    email_client             = request.POST['inputEmailFrom']
    asunto                   = request.POST['inputSubject']
    mensaje                  = request.POST['inputMessage']
    correo                   = EmailMessage(
        subject=f'BIOCOLIBRISTORE - {asunto}',
        body=f'Cliente ==> {nombres} {apellidos}\nCorreo Electrónico ==> {email_client}\n\n{mensaje}',
        from_email=settings.EMAIL_HOST_USER,
        cc=[email_client],
        bcc=[settings.ADMIN_EMAIL]
    )
    return nombres, apellidos, email_client, mensaje, asunto, correo


def __save_contact(name, last_name, email, message, subject):
    Contacto(
        nombre_cliente=name,
        apellido_cliente=last_name,
        email_remitente=email,
        mensaje=message,
        asunto=subject
    ).save()