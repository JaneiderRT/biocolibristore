# Generated by Django 3.2 on 2024-11-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_contacto_dni_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='asunto',
            field=models.CharField(default='Sin Asunto', max_length=100),
        ),
    ]
