from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models
from . import forms

class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['first_name'].required = True
        form.base_fields['last_name'].required = True
        form.base_fields['email'].required = True
        return form


class MetodosPagoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)


class PorcentajesAdmin(admin.ModelAdmin):
    ordering = ('titulo',)
    list_display = ('titulo', 'descripcion', 'valor',)
    search_fields = ('titulo',)


class TipoDocumentoAdmin(admin.ModelAdmin):
    ordering = ('descripcion',)
    list_display = ('descripcion', 'abreviacion',)


class TipoPersonaAdmin(admin.ModelAdmin):
    ordering = ('descripcion',)
    list_display = ('descripcion', 'abreviacion',)


class GeneroAdmin(admin.ModelAdmin):
    ordering = ('descripcion',)
    list_display = ('descripcion', 'abreviacion',)


class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)


class AsosciadoAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    list_display = ('dni', 'nombre', 'email', 'contacto', 'num_cuenta',)
    list_filter = ('id_tipo_dni',)
    search_fields = ('dni', 'nombre',)


class ProductoAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    list_display = ('nombre', 'id_categoria', 'precio',)
    list_filter = ('id_categoria', 'precio',)
    search_fields = ('nombre', 'id_categoria__descripcion', 'precio',)
    readonly_fields = ('fecha_creacion', 'fecha_edicion',)


class AdministradorAdmin(admin.ModelAdmin):
    ordering = ('nombres',)
    list_display = ('dni', 'nombres', 'apellidos', 'email', 'contacto', 'usuario',)
    list_filter = ('genero', 'id_tipo_dni', 'id_tipo_persona',)
    search_fields = ('nombres', 'apellidos', 'dni',)
    form = forms.AdministradorAdminForm


class ClienteAdmin(admin.ModelAdmin):
    ordering = ('nombres',)
    list_display = ('dni', 'nombres', 'apellidos', 'email', 'contacto', 'domicilio', 'num_cuenta', 'usuario',)
    list_filter = ('genero', 'id_tipo_dni', 'id_tipo_persona',)
    form = forms.ClienteAdminForm
    #readonly_fields = ('dni', 'id_tipo_dni', 'nombres', 'apellidos', 'genero', 'email', 'contacto', 'domicilio', 'id_tipo_persona', 'num_cuenta', 'usuario',)


class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('dni_cliente', 'show_products', 'sub_total', 'iva', 'total', 'fecha_orden',)
    readonly_fields = ('id_producto', 'dni_cliente', 'sub_total', 'iva', 'total', 'fecha_orden',)

    def show_products(self, obj):
        return ' - '.join([str(p) for p in obj.id_producto.all()])
    
    show_products.short_description = 'Detalle'


class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('dni_cliente', 'id_pago', 'estado', 'estado_envio',)
    readonly_fields = ('dni_cliente', 'id_pago', 'estado', 'estado_envio',)
    list_filter = ('estado', 'estado_envio',)


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Modelos que va a poder topar el administrador.
admin.site.register(models.Metodos_Pago, MetodosPagoAdmin)
admin.site.register(models.Porcentajes, PorcentajesAdmin)
admin.site.register(models.Ref_Tipo_Documento, TipoDocumentoAdmin)
admin.site.register(models.Ref_Tipo_Persona, TipoPersonaAdmin)
admin.site.register(models.Genero, GeneroAdmin)
admin.site.register(models.Categoria_Producto, CategoriaProductoAdmin)
admin.site.register(models.Asosciado, AsosciadoAdmin)
admin.site.register(models.Producto, ProductoAdmin)

# Modelos que no va a poder topar el administrador.
admin.site.register(models.Administrador, AdministradorAdmin)
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Detalle_Orden, DetalleOrdenAdmin)
admin.site.register(models.Pago)
admin.site.register(models.Orden_Compra, OrdenCompraAdmin)
admin.site.register(models.Historial_Inversiones)
admin.site.register(models.Historial_Ganancias)
