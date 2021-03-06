# Generated by Django 3.2.13 on 2022-07-02 17:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0013_user_following'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Correctivo', 'MC'), ('Preventivo', 'MP')], db_index=True, max_length=200, verbose_name='Tipo de mantenimiento')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Categoria de Mantenimiento',
                'verbose_name_plural': 'Categorias de Mantenimientos',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Coti_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coti_code', models.CharField(choices=[('CMC', 'CMC'), ('CMP', 'CMP'), ('CSE', 'CSE'), ('CSR', 'CSR')], max_length=3, null=True)),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('RUC2', models.CharField(max_length=100, verbose_name='RUC')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('aprobe', models.BooleanField(default=True)),
                ('dias', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('price2', models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True, verbose_name='valor de anticipo de la Cotización')),
                ('price3', models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True, verbose_name='valor de pendiente de la Cotización')),
                ('Iva2', models.PositiveSmallIntegerField(default=12)),
                ('code', models.CharField(blank=True, max_length=1000000)),
                ('building_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edificio_2.category')),
            ],
            options={
                'verbose_name': 'Orden de Compra',
                'verbose_name_plural': 'Ordenes de Compras',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coti_code', models.CharField(choices=[('CMC', 'CMC'), ('CMP', 'CMP'), ('CSE', 'CSE'), ('CSR', 'CSR')], max_length=3, null=True)),
                ('name', models.CharField(blank=True, db_index=True, max_length=1000000, null=True, verbose_name='Nombre de Proyecto')),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('item', models.CharField(blank=True, max_length=1000)),
                ('description', models.CharField(blank=True, max_length=1000000, null=True)),
                ('Units', models.CharField(choices=[('mL', 'ml'), ('m^2', 'm^2'), ('Kg', 'Kg'), ('Gl', 'Gl')], max_length=3, null=True)),
                ('image', models.ImageField(blank=True, upload_to='image_item/%Y/%m/%d', verbose_name='Imagenes Reportadas')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True, verbose_name='Disponible')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Valor Unitario')),
                ('iva', models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('quantity', models.PositiveIntegerField(default=1, null=True)),
                ('updated_a', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de última actualización de anticipo')),
                ('anticipo', models.PositiveIntegerField(default=50, null=True, verbose_name='Anticipo')),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('code', models.CharField(blank=True, max_length=1000000)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='edificio_2.category', verbose_name='Categoria de Mantenimiento')),
            ],
            options={
                'verbose_name': 'la Cotización de Proyectos',
                'verbose_name_plural': 'Cotización de Proyectos',
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Project_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_code', models.CharField(choices=[('CMC', 'CMC'), ('CMP', 'CMP'), ('CSE', 'CSE'), ('CSR', 'CSR')], max_length=3, null=True)),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('RUC2', models.CharField(max_length=100, verbose_name='RUC')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('aprobe', models.BooleanField(default=True)),
                ('dias', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('price1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Iva2', models.PositiveSmallIntegerField(default=12)),
                ('code', models.CharField(blank=True, max_length=1000000)),
                ('building_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edificio_2.category')),
                ('coti', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edificio_2.cotizacion')),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Proyectos',
                'verbose_name_plural': 'Proyectos',
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Project_OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('anticipo', models.PositiveIntegerField(default=50, verbose_name='anticipo')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='edificio_2.coti_order')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='edificio_2.project_order')),
            ],
        ),
        migrations.CreateModel(
            name='Coti_OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('anticipo', models.PositiveIntegerField(default=50, verbose_name='anticipo')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='edificio_2.cotizacion')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='edificio_2.coti_order')),
            ],
        ),
        migrations.AddField(
            model_name='coti_order',
            name='coti',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edificio_2.cotizacion'),
        ),
        migrations.AddField(
            model_name='coti_order',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='coti_order',
            index_together={('id', 'slug')},
        ),
    ]
