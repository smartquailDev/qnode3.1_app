# Generated by Django 3.2.13 on 2022-08-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_2', '0011_auto_20220829_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coti_order',
            name='price1',
            field=models.DecimalField(decimal_places=2, max_digits=1000, null=True),
        ),
    ]
