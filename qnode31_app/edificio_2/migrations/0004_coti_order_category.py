# Generated by Django 3.2.13 on 2022-06-20 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_2', '0003_coti_order_coti_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='coti_order',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edificio_2.category'),
        ),
    ]
