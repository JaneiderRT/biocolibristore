# Generated by Django 3.2 on 2025-01-21 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20250118_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria_producto',
            old_name='cod_catgoria',
            new_name='cod_categoria',
        ),
    ]
