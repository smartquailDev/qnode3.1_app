# Generated by Django 3.1.5 on 2021-02-09 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HOMEDETAIL', '0003_auto_20210209_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='Edificio',
        ),
    ]
