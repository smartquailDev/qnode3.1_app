# Generated by Django 3.1.5 on 2021-02-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProFit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maintenance_type', models.CharField(max_length=50, verbose_name='Maintenance Type')),
                ('activity', models.CharField(max_length=50, verbose_name='Activity')),
                ('Description', models.TextField()),
            ],
            options={
                'verbose_name': 'Contizacion ProFit',
                'verbose_name_plural': 'Cotizaciones ProFits',
                'ordering': ('-activity',),
            },
        ),
    ]
