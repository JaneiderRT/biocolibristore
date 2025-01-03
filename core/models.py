from django.db import models

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
        return f'Porcentaje De {self.titulo} - {self.valor} %'

    class Meta:
        verbose_name_plural = 'Porcentajes'


class Ref_Tipo_Documento(models.Model):
    cod_tipo_documento = models.BigAutoField(auto_created=True, primary_key=True)
    abreviacion        = models.CharField(max_length=3)
    descripcion        = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Tipo De Documentos'


class Ref_Tipo_Persona(models.Model):
    cod_tipo_persona = models.BigAutoField(auto_created=True, primary_key=True)
    abreviacion      = models.CharField(max_length=2)
    descripcion      = models.CharField(max_length=16)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Tipo De Personas'


class Administrador(models.Model):
    dni             = models.IntegerField(primary_key=True)
    id_tipo_dni     = models.ForeignKey(Ref_Tipo_Documento, on_delete=models.CASCADE, related_name='adm_documento')
    nombres         = models.CharField(max_length=30)
    apellidos       = models.CharField(max_length=30)
    genero          = models.CharField(max_length=1)
    email           = models.EmailField()
    contacto        = models.CharField(max_length=10)
    domicilio       = models.CharField(max_length=100, blank=True, null=True)
    id_tipo_persona = models.ForeignKey(Ref_Tipo_Persona, on_delete=models.CASCADE, related_name='adm_persona')

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    class Meta:
        verbose_name_plural = 'Administrador'


class Cliente(models.Model):
    dni             = models.IntegerField(primary_key=True)
    id_tipo_dni     = models.ForeignKey(Ref_Tipo_Documento, on_delete=models.CASCADE, related_name='cli_documento')
    nombres         = models.CharField(max_length=30)
    apellidos       = models.CharField(max_length=30)
    genero          = models.CharField(max_length=1)
    email           = models.EmailField()
    contacto        = models.CharField(max_length=10)
    domicilio       = models.CharField(max_length=100)
    id_tipo_persona = models.ForeignKey(Ref_Tipo_Persona, on_delete=models.CASCADE, related_name='cli_persona')
    num_cuenta      = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'


class Asosciado(models.Model):
    dni             = models.IntegerField(primary_key=True)
    id_tipo_dni     = models.ForeignKey(Ref_Tipo_Documento, on_delete=models.CASCADE, related_name='aso_documento')
    nombre          = models.CharField(max_length=30)
    email           = models.EmailField()
    contacto        = models.CharField(max_length=10)
    id_tipo_persona = models.ForeignKey(Ref_Tipo_Persona, on_delete=models.CASCADE, related_name='aso_persona')
    num_cuenta      = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Categoria_Producto(models.Model):
    cod_catgoria = models.BigAutoField(auto_created=True, primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Categoria De Productos'


class Producto(models.Model):
    cod_producto   = models.BigAutoField(auto_created=True, primary_key=True)
    nombre         = models.CharField(max_length=30)
    id_categoria   = models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE, related_name='categoria')
    descripcion    = models.TextField(max_length=255)
    precio         = models.FloatField()
    imagen         = models.ImageField(upload_to='productos/%d/%m/%Y/')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion Producto')
    fecha_edicion  = models.DateTimeField(auto_now=True, verbose_name='Fecha Edicion Producto')

    def __str__(self):
        return f'{self.nombre} - {self.id_categoria}'

    class Meta:
        ordering = ['cod_producto']


class Detalle_Orden(models.Model):
    cod_orden   = models.BigAutoField(auto_created=True, primary_key=True)
    fecha_orden = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion Orden')
    id_producto = models.ManyToManyField(Producto, related_name='do_producto')
    dni_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='do_cliente')
    sub_total   = models.FloatField()
    iva         = models.PositiveSmallIntegerField()
    total       = models.FloatField()

    def __str__(self):
        return f'{self.cod_orden} | {self.fecha_orden} - {self.dni_cliente}'

    class Meta:
        verbose_name_plural = 'Detalles De Orden'


class Pago(models.Model):
    cod_pago    = models.BigAutoField(auto_created=True, primary_key=True)
    id_metodo   = models.ForeignKey(Metodos_Pago, on_delete=models.CASCADE, related_name='pago_metodo')
    id_orden    = models.OneToOneField(Detalle_Orden, on_delete=models.CASCADE)
    dni_cliente = models.IntegerField()
    fecha_pago  = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion Pago')

    def __str__(self):
        return f'{self.cod_pago} | {self.id_orden} - {self.dni_cliente}'


class Orden_Compra(models.Model):
    dni_cliente  = models.IntegerField()
    id_pago      = models.OneToOneField(Pago, on_delete=models.CASCADE)
    estado       = models.CharField(max_length=20)
    estado_envio = models.CharField(max_length=20)

    def __str__(self):
        return f'Pago: {self.id_pago} - {self.dni_cliente}'

    class Meta:
        verbose_name_plural = 'Ordenes De Compra'


class Historial_Inversiones(models.Model):
    cod_inversion   = models.BigAutoField(auto_created=True, primary_key=True)
    dni_cliente     = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    id_orden        = models.OneToOneField(Orden_Compra, on_delete=models.CASCADE)
    dni_asociado    = models.OneToOneField(Asosciado, on_delete=models.CASCADE)
    fecha_inversion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion Inversion')
    estado          = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.cod_inversion} - {self.dni_cliente}'

    class Meta:
        verbose_name_plural = 'Historial De Inversiones'


class Historia_Ganancias(models.Model):
    cod_ganancias   = models.BigAutoField(auto_created=True, primary_key=True)
    dni_cliente     = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    id_inversion    = models.OneToOneField(Historial_Inversiones, on_delete=models.CASCADE)
    dni_asociado    = models.OneToOneField(Asosciado, on_delete=models.CASCADE)
    fecha_ganancia  = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion Ganancia')
    estado          = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.cod_ganancias} | {self.dni_cliente}'

    class Meta:
        verbose_name_plural = 'Historial De Ganancias'


class Contacto(models.Model):
    cod_mensaje      = models.IntegerField(auto_created=True, primary_key=True)
    nombre_cliente   = models.CharField(max_length=30)
    apellido_cliente = models.CharField(max_length=30)
    email_remitente  = models.EmailField()
    asunto           = models.CharField(max_length=100, default='Sin Asunto')
    mensaje          = models.TextField(max_length=800)
    fecha_creacion   = models.DateTimeField(verbose_name='Fecha Creacion Mensaje')

    def __str__(self):
        return f'Mensaje #{self.cod_mensaje} | {self.nombre_cliente}  {self.apellido_cliente}'

    class Meta:
        verbose_name_plural = 'Contacto'
