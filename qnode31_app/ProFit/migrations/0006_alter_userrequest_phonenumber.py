# Generated by Django 3.2.13 on 2022-05-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProFit', '0005_userrequest_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='phonenumber',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
