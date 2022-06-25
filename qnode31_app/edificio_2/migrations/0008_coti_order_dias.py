# Generated by Django 3.2.13 on 2022-06-24 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_2', '0007_coti_order_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coti_order',
            name='dias',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)]),
        ),
    ]
