# Generated by Django 3.1.5 on 2021-02-05 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20210205_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_payment',
            name='Numero_de_cheque',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)], verbose_name='Numero de Cheque'),
        ),
        migrations.AlterField(
            model_name='check_payment',
            name='Numero_de_control',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)], verbose_name='Numero de Control'),
        ),
        migrations.AlterField(
            model_name='check_payment',
            name='fecha_de_emision',
            field=models.DateTimeField(verbose_name='Fecha de emisón'),
        ),
    ]
