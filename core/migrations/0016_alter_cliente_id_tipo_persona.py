# Generated by Django 3.2 on 2025-01-24 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_cliente_id_tipo_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_tipo_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cli_persona', to='core.ref_tipo_persona'),
        ),
    ]
