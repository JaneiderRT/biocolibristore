from django.contrib import admin

from . import models

# Register your models here.
# Modelos que va a poder topar el administrador.
admin.site.register(models.Metodos_Pago)
admin.site.register(models.Porcentajes)
admin.site.register(models.Ref_Tipo_Documento)
admin.site.register(models.Ref_Tipo_Persona)
admin.site.register(models.Categoria_Producto)
admin.site.register(models.Cliente)
admin.site.register(models.Asosciado)
admin.site.register(models.Producto)
admin.site.register(models.Orden_Compra)

# Modelos que no va a poder topar el administrador.
admin.site.register(models.Administrador)
admin.site.register(models.Detalle_Orden)
admin.site.register(models.Pago)
admin.site.register(models.Historial_Inversiones)
admin.site.register(models.Historia_Ganancias)
