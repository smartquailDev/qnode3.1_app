# Generated by Django 3.1.5 on 2022-01-26 17:15

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='service_info4',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Información de servicio-4'),
        ),
    ]
