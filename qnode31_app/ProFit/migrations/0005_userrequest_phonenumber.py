# Generated by Django 3.2.13 on 2022-05-28 18:56

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ProFit', '0004_remove_userrequest_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
