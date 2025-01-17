from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Administrador, Cliente

@receiver(post_save, sender=Administrador)
def create_admin(sender, instance, created, **kwargs):
    if created:
        instance.nombres = instance.usuario.first_name
        instance.apellidos = instance.usuario.last_name
        instance.save()

@receiver(post_save, sender=Cliente)
def create_client(sender, instance, created, **kwargs):
    if created:
        instance.nombres = instance.usuario.first_name
        instance.apellidos = instance.usuario.last_name
        instance.save()