# Generated by Django 3.2 on 2025-01-18 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20250103_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('cod_genero', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('abreviacion', models.CharField(max_length=1)),
                ('descripcion', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.AlterField(
            model_name='administrador',
            name='apellidos',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='nombres',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellidos',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='num_cuenta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adm_genero', to='core.genero'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cli_genero', to='core.genero'),
        ),
    ]
