# Generated by Django 3.1.5 on 2021-01-31 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mantenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Correctivo', 'PMC'), ('Preventivo', 'PMP'), ('Correctivo Sistema de Emergencia', 'PCSE'), ('Correctivo Sistema de Revestimientos', 'PCSR')], db_index=True, max_length=200, null=True, verbose_name='Tipo de Mantenimiento')),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Mantenimiento',
                'verbose_name_plural': 'Tipo de Mantenimientos',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_name', models.CharField(choices=[('Home Detail', 'Home Detail'), ('Habitad', 'Habitad')], db_index=True, max_length=200, null=True, verbose_name='Nombre de Aliado')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Nombre de Proyecto')),
                ('code2', models.CharField(blank=True, max_length=500, verbose_name='Codigo de Proyecto')),
                ('description', models.TextField(blank=True, verbose_name='Descripción de Proyecto')),
                ('image', models.ImageField(blank=True, upload_to='main/%Y/%m/%d', verbose_name='Imagenes Reportadas')),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Unitario')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Cantidad [m2]')),
                ('available', models.BooleanField(default=True, verbose_name='Aprobado?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación de proyecto')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de última actualización de proyecto')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main', to='Proyectos.mantenimiento', verbose_name='Categoría de Mantenimiento')),
            ],
            options={
                'verbose_name': 'Proyectos para Aliados',
                'verbose_name_plural': 'Proyecto para Aliados',
                'index_together': {('id', 'slug')},
            },
        ),
    ]
