# Generated by Django 3.2 on 2025-01-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_rename_cod_catgoria_categoria_producto_cod_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellidos',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_edicion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha Edicion'),
        ),
    ]
