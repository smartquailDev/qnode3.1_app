# Generated by Django 3.2.13 on 2022-05-27 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProFit', '0003_auto_20220527_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrequest',
            name='phonenumber',
        ),
    ]
