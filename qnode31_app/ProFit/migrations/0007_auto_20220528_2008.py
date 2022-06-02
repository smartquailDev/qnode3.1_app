# Generated by Django 3.2.13 on 2022-05-28 20:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ProFit', '0006_alter_userrequest_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='admin_user',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre completo del administrador:'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='direccion',
            field=models.CharField(max_length=50, null=True, verbose_name='Dirección del edificio'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='edificio',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre del Edificio:'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Teléfono de contacto'),
        ),
    ]