# Generated by Django 3.2.13 on 2022-07-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_2', '0003_alter_coti_order_price1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coti_order',
            name='aprobe',
            field=models.BooleanField(default=False),
        ),
    ]
