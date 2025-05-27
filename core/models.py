from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Metodos_Pago(models.Model):
    cod_metodo  = models.BigAutoField(auto_created=True, primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Metodos De Pago'


class Porcentajes(models.Model):
    id_procentaje = models.BigAutoField(auto_created=True, primary_key=True)
    titulo        = models.CharField(max_length=50)
    descripcion   = models.TextField(max_length=255)
    valor         = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.titulo} - {self.valor} %'

    class Meta:
        verbose_name_plural = 'Porcentajes'


class Ref_Tipo_Documento(models.Model):
    cod_tipo_documento = models.BigAutoField(auto_created=True, primary_key=True)
    abreviacion        = models.CharField(max_length=3)
    descripcion        = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cod_tipo_documento} - {self.descripcion}'

    class Meta:
        verbose_name_plural = 'Tipo De Documentos'


class Ref_Tipo_Persona(models.Model):
    cod_tipo_persona = models.BigAutoField(auto_created=True, primary_key=True)
    abreviacion      = models.CharField(max_length=2)
    descripcion      = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.cod_tipo_persona} - {self.descripcion}'

    class Meta:
        verbose_name_plural = 'Tipo De Personas'


class Genero(models.Model):
    cod_genero  = models.BigAutoField(auto_created=True, primary_key=True)
    abreviacion = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.cod_genero} - {self.descripcion}'
    
    class Meta:
        verbose_name_plural = 'Generos'


class Administrador(models.Model):
    dni             = models.IntegerField(primary_key=True)
    id_tipo_dni     = models.ForeignKey(Ref_Tipo_Documento, on_delete=models.CASCADE, related_name='adm_documento', verbose_name='Tipo Documento')
    nombres         = models.CharField(max_length=100, blank=True)
    apellidos       = models.CharField(max_length=100, blank=True)
    genero          = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='adm_genero')
    email           = models.EmailField(blank=True)
    contacto        = models.CharField(max_length=10)
    domicilio       = models.CharField(max_length=100, blank=True, null=True)
    id_tipo_persona = models.ForeignKey(Ref_Tipo_Persona, on_delete=models.CASCADE, related_name='adm_persona', verbose_name='Tipo Persona')
    usuario         = models.OneToOneField(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    class Meta:
        verbose_name_plural = 'Administrador'


class Cliente(models.Model):
    dni             = models.IntegerField(primary_key=True)
    id_tipo_dni     = models.ForeignKey(Ref_Tipo_Documento, on_delete=models.CASCADE, related_name='cli_documento', verbose_name='Tipo Documento')
    nombres         = models.CharField(max_length=100, blank=True)
    apellidos       = models.CharField(max_length=100, null=True, blank=True)
    genero          = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='cli_genero')
    email           = models.EmailField(blank=True)
    contacto        = models.CharField(max_length=10)
    domicilio       = models.CharField(max_length=100)
    id_tipo_persona = models.ForeignKey(Ref_Tipo_Persona, on_delete=models.CASCADE, related_name='cli_persona', verbose_name='Tipo Persona')
    num_cuenta      = models.CharField(max_length=20, null=True, blank=True)
    usuario         = models.OneToOneField(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'


class Asosciado(models.Model):
    dni             = models.IntegerField(primary_key=True)
    id_tipo_dni     = models.ForeignKey(Ref_Tipo_Documento, on_delete=models.CASCADE, related_name='aso_documento', verbose_name='Tipo Documento')
    nombre          = models.CharField(max_length=30)
    email           = models.EmailField()
    contacto        = models.CharField(max_length=10)
    id_tipo_persona = models.ForeignKey(Ref_Tipo_Persona, on_delete=models.CASCADE, related_name='aso_persona', verbose_name='Tipo Persona')
    num_cuenta      = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Categoria_Producto(models.Model):
    cod_categoria = models.BigAutoField(auto_created=True, primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Categoria De Productos'


class Producto(models.Model):
    cod_producto   = models.BigAutoField(auto_created=True, primary_key=True)
    nombre         = models.CharField(max_length=30)
    id_categoria   = models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE, related_name='categoria', verbose_name='Categoria')
    descripcion    = models.TextField(max_length=255)
    precio         = models.FloatField()
    imagen         = models.ImageField(upload_to='productos/%d/%m/%Y/')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')
    fecha_edicion  = models.DateTimeField(auto_now=True, verbose_name='Fecha Edicion')

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        ordering = ['cod_producto']


class Detalle_Orden(models.Model):
    cod_orden   = models.BigAutoField(auto_created=True, primary_key=True)
    fecha_orden = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')
    id_producto = models.ManyToManyField(Producto, related_name='do_producto', verbose_name='Detalle')
    dni_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='do_cliente', verbose_name='Cliente')
    sub_total   = models.FloatField()
    iva         = models.PositiveSmallIntegerField()
    total       = models.FloatField()

    def __str__(self):
        return self.cod_orden

    class Meta:
        verbose_name_plural = 'Detalles De Orden'


class Pago(models.Model):
    cod_pago    = models.BigAutoField(auto_created=True, primary_key=True)
    id_metodo   = models.ForeignKey(Metodos_Pago, on_delete=models.CASCADE, related_name='pago_metodo', verbose_name='Metodo Pago')
    id_orden    = models.OneToOneField(Detalle_Orden, on_delete=models.CASCADE, verbose_name='Detalle Orden')
    dni_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pago_cliente', verbose_name='Cliente')
    fecha_pago  = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')

    def __str__(self):
        return self.cod_pago


class Orden_Compra(models.Model):
    dni_cliente      = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='oc_cliente', verbose_name='Cliente')
    id_pago          = models.OneToOneField(Pago, on_delete=models.CASCADE, related_name='oc_pago', verbose_name='Codigo Pago')
    estado           = models.CharField(max_length=20, verbose_name='Estado Compra')
    estado_envio     = models.CharField(max_length=20, verbose_name='Estado Envio')

    def __str__(self):
        return self.cod_orden_compra

    class Meta:
        verbose_name_plural = 'Ordenes De Compra'


class Historial_Inversiones(models.Model):
    cod_inversion   = models.BigAutoField(auto_created=True, primary_key=True)
    dni_cliente     = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='hi_cliente', verbose_name='Cliente')
    id_orden        = models.OneToOneField(Orden_Compra, on_delete=models.CASCADE, related_name='hi_orden', verbose_name='Orden Compra')
    dni_asociado    = models.OneToOneField(Asosciado, on_delete=models.CASCADE, related_name='hi_asociado', verbose_name='Asociado')
    fecha_inversion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Inversión')
    estado          = models.CharField(max_length=20, verbose_name='Estado Inversión')
    valor_inversion = models.FloatField(verbose_name='Valor Inversión', default=0)

    def __str__(self):
        return self.cod_inversion

    class Meta:
        verbose_name_plural = 'Historial De Inversiones'


class Historial_Ganancias(models.Model):
    cod_ganancias   = models.BigAutoField(auto_created=True, primary_key=True)
    dni_cliente     = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='hg_cliente', verbose_name='Cliente')
    id_inversion    = models.OneToOneField(Historial_Inversiones, on_delete=models.CASCADE, related_name='hg_inversion', verbose_name='Inversion')
    dni_asociado    = models.OneToOneField(Asosciado, on_delete=models.CASCADE, related_name='hg_asociado', verbose_name='Asociado')
    fecha_ganancia  = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Ganancia')
    estado          = models.CharField(max_length=20, verbose_name='Estado Ganancia')
    valor_ganancia  = models.FloatField(verbose_name='Valor Ganancia')

    def __str__(self):
        return self.cod_ganancias

    class Meta:
        verbose_name_plural = 'Historial De Ganancias'


class Contacto(models.Model):
    cod_mensaje      = models.IntegerField(auto_created=True, primary_key=True)
    nombre_cliente   = models.CharField(max_length=30)
    apellido_cliente = models.CharField(max_length=30)
    email_remitente  = models.EmailField()
    asunto           = models.CharField(max_length=100, default='Sin Asunto')
    mensaje          = models.TextField(max_length=800)
    fecha_creacion   = models.DateTimeField(verbose_name='Fecha Creacion')

    def __str__(self):
        return self.cod_mensaje

    class Meta:
        verbose_name_plural = 'Contacto'
