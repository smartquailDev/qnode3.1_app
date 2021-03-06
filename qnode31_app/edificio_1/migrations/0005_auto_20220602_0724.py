# Generated by Django 3.2.13 on 2022-06-02 07:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_1', '0004_auto_20220602_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.BigIntegerField(null=True, verbose_name='Escriba su codigo único de aprobación')),
                ('email', models.EmailField(max_length=254, verbose_name='Escriba su correo electrico')),
                ('aprobe', models.BooleanField(default=False, verbose_name='Aprobado')),
                ('diss', models.BooleanField(default=False, verbose_name='rechazado')),
                ('iva', models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'ordering': ('-email',),
            },
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='coti',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='edificio_1.cotizacion'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='edificio_1.order_cotizacion'),
        ),
    ]
