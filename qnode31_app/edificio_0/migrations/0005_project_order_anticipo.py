# Generated by Django 3.2.13 on 2022-08-30 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_0', '0004_project_order_project_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_order',
            name='anticipo',
            field=models.PositiveIntegerField(default=50, null=True, verbose_name='Anticipo'),
        ),
    ]
