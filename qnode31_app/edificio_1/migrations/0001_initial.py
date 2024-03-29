# Generated by Django 3.2.13 on 2022-06-02 02:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProFit', '0008_profile_edificio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenace_type', models.CharField(choices=[('MC', 'Mantenimiento Correctivo'), ('MP', 'Mantenimiento Preventivo')], db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Categoria de Mantenimiento',
                'verbose_name_plural': 'Categorias de Mantenimientos',
                'ordering': ('maintenace_type',),
            },
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coti_code', models.CharField(choices=[('CMC', 'CMC'), ('CMP', 'CMP'), ('CSE', 'CSE'), ('CSR', 'CSR')], max_length=3, null=True)),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='image_item/%Y/%m/%d', verbose_name='Imagenes Reportadas')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True, verbose_name='Aprobado?')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Valor Unitario')),
                ('iva', models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('code', models.CharField(blank=True, max_length=1000000)),
                ('Edificio', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProFit.profile')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='edificio_1.category', verbose_name='Categoria de Mantenimiento')),
            ],
            options={
                'verbose_name': 'la Cotización de Proyectos',
                'verbose_name_plural': 'Cotización de Proyectos',
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Diagnostico de Mantenimiento',
                'verbose_name_plural': 'Diagnostico de Mantenimiento',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProFit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maintenance_type', models.CharField(choices=[('Correctivo', 'Correctivo'), ('Preventivo', 'Preventivo'), ('Revestimientos y Pintura', 'Revestimientos y Pintura'), ('Sistema de emergencia', 'Sistema de emergencia'), ('Remodelación', 'Remodelación'), ('Refacción', 'Refacción')], max_length=500, null=True, verbose_name='Maintenance Type')),
                ('activity', models.CharField(choices=[('Albañilería', 'Albañilería'), ('Plomería', 'Plomería'), ('Electricidad', 'Electricidad'), ('Hidráulica', 'Hidráulica'), ('Electromecánica', 'Electromecánica'), ('Luminaria', 'Luminaria'), ('Limpieza y Desinfección', 'Limpieza y Desinfección')], max_length=500, null=True, verbose_name='Activity')),
                ('Maintenance_Zone', models.CharField(choices=[('Bombas de agua', 'Bombas de agua'), ('Calderos', 'Calderos'), ('Generadores Eléctricos', 'Generadores Eléctricos'), ('Ingresos', 'Ingresos'), ('Parqueaderos', 'Parqueaderos'), ('Ascensores', 'Ascensores'), ('Area comunal', 'Area Comunal'), ('Departamento particular', 'Departamento particular'), ('Terraza', 'Terraza')], max_length=500, null=True, verbose_name='Maintenance Zone')),
                ('Description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de solicitud')),
                ('visit', models.DateTimeField(null=True, verbose_name='visita técnica')),
            ],
            options={
                'verbose_name': 'Solicitud de Contizacion ProFit',
                'verbose_name_plural': 'Solicitudes de Cotizaciones ProFits',
                'ordering': ('-activity',),
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=3, null=True, verbose_name='Codigo de Proyecto')),
                ('invoice_code', models.CharField(max_length=3, null=True, verbose_name='Codigo de Cotización')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de Creación')),
                ('Fecha', models.DateField(null=True, verbose_name='Fecha de entrega de Proyecto')),
                ('porcet2', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Avance de Obra %')),
                ('porcet', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Porcetanje de Anticipo %')),
                ('value2', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Valor neto de la cotización')),
                ('value3', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('value4', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Seguimiento de Proyecto',
                'verbose_name_plural': 'Seguimiento de Proyecto',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('Unit', models.CharField(choices=[('mL', 'ml'), ('m^2', 'm^2'), ('Kg', 'Kg'), ('Gl', 'Gl')], max_length=3, null=True)),
                ('coti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='edificio_1.cotizacion')),
            ],
        ),
        migrations.CreateModel(
            name='ProyectosHomeDetail',
            fields=[
            ],
            options={
                'verbose_name': 'Seguimiento de Proyecto',
                'verbose_name_plural': 'Seguimiento de Proyecto',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('edificio_1.proyecto',),
        ),
        migrations.CreateModel(
            name='DiagnosticoTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('report_code', models.CharField(choices=[('RMC', 'RMC'), ('RMP', 'RMP'), ('RSE', 'RSE'), ('RSR', 'RSR')], max_length=3, verbose_name='Report Code')),
                ('report_id', models.CharField(max_length=2, verbose_name='Report ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date report Created')),
                ('date_meet', models.DateTimeField(null=True, verbose_name='Date Technical meet')),
                ('project_name2', models.CharField(help_text='Escribir Nombre de Proyecto', max_length=50, verbose_name='Project name')),
                ('item_description', models.TextField(blank=True, null=True, verbose_name='Item description')),
                ('image_item', models.ImageField(blank=True, null=True, upload_to='static/edificios/', verbose_name='image Item')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Unitario')),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Cantidad')),
                ('Unit', models.CharField(blank=True, choices=[('mL', 'ml'), ('m^2', 'm^2'), ('Kg', 'Kg'), ('Gl', 'Gl')], max_length=3, null=True, verbose_name='Unidades')),
                ('iva', models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('promain_code', models.CharField(help_text='Codigo de Tecnico Profix Responsable', max_length=20, verbose_name='ProMain Code')),
                ('dayswork', models.IntegerField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(15)], verbose_name='Calendary days')),
                ('code', models.CharField(blank=True, max_length=10, verbose_name='codigo')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='edificio_1.diagnostico')),
            ],
            options={
                'verbose_name': 'Diagnostico de Mantenimiento Translation',
                'db_table': 'edificio_1_diagnostico_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
