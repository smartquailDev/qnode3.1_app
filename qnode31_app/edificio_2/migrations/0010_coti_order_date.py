# Generated by Django 3.2.13 on 2022-06-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_2', '0009_auto_20220624_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='coti_order',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
