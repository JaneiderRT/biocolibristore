from django.conf import settings
from django.core.mail import EmailMessage

from .models import Contacto

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