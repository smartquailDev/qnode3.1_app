# Generated by Django 3.1.5 on 2021-03-01 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0010_auto_20210228_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='anticipo',
            field=models.PositiveIntegerField(default=50, verbose_name='Anticipo'),
        ),
    ]
