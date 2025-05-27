from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Cliente, Administrador

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class ClienteAdminForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['nombres', 'apellidos', 'email']


class AdministradorAdminForm(forms.ModelForm):
    class Meta:
        model = Administrador
        exclude = ['nombres', 'apellidos', 'email']