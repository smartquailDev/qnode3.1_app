# Generated by Django 3.2.13 on 2022-08-24 17:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_2', '0008_auto_20220712_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_order',
            name='category',
        ),
        migrations.RemoveField(
            model_name='project_order',
            name='coti',
        ),
        migrations.AlterField(
            model_name='project_order',
            name='project_code',
            field=models.CharField(choices=[('PMC', 'PMC'), ('PMP', 'PMP'), ('PSE', 'PSE'), ('PSR', 'PSR')], max_length=3, null=True),
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_code', models.CharField(choices=[('PMC', 'PMC'), ('PMP', 'PMP'), ('PSE', 'PSE'), ('PSR', 'PSR')], max_length=3, null=True)),
                ('name', models.CharField(blank=True, db_index=True, max_length=1000000, null=True, verbose_name='Nombre de Proyecto')),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('item', models.CharField(blank=True, max_length=1000)),
                ('description', models.CharField(blank=True, max_length=1000000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='image_item/%Y/%m/%d', verbose_name='Imagenes Reportadas')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True, verbose_name='Disponible')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Valor Unitario')),
                ('iva', models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('quantity', models.PositiveIntegerField(default=1, null=True)),
                ('updated_a', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de última actualización de anticipo')),
                ('anticipo', models.PositiveIntegerField(default=50, null=True, verbose_name='Anticipo')),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('code', models.CharField(blank=True, max_length=1000000)),
            ],
            options={
                'verbose_name': 'la Cotización de Proyectos',
                'verbose_name_plural': 'Cotización de Proyectos',
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='project_order',
            name='proc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edificio_2.project'),
        ),
        migrations.AlterField(
            model_name='project_orderitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='edificio_2.project'),
        ),
    ]
