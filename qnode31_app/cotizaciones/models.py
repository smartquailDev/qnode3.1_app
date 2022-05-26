from django.db import models
from django import forms
from decimal import Decimal
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class ProFit(models.Model):
    CHOICE=[('Correctivo','Correctivo'),
    ('Preventivo','Preventivo'),
    ('Revestimientos y Pintura','Revestimientos y Pintura'),
    ('Sistema de emergencia','Sistema de emergencia'),
    ('Remodelación','Remodelación'),
    ('Refacción','Refacción'),
    ]
    CHOICE2=[('Albañilería','Albañilería'),
    ('Plomería','Plomería'),
    ('Electricidad','Electricidad'),
    ('Hidráulica','Hidráulica'),
    ('Electromecánica','Electromecánica'),
    ('Luminaria','Luminaria'),
    ('Limpieza y Desinfección','Limpieza y Desinfección'),
    ]
    CHOICE3=[('Bombas de agua','Bombas de agua'),
    ('Calderos','Calderos'),
    ('Generadores Eléctricos','Generadores Eléctricos'),
    ('Ingresos','Ingresos'),
    ('Parqueaderos','Parqueaderos'),
    ('Ascensores','Ascensores'),
    ('Area comunal','Area Comunal'),
    ('Departamento particular','Departamento particular'),
    ('Terraza','Terraza'),
    ]

    Maintenance_type = models.CharField(_('Maintenance Type'), max_length=500 , choices=CHOICE,null=True)
    activity = models.CharField(_('Activity'), max_length=500, choices=CHOICE2,null=True)
    Maintenance_Zone = models.CharField(_('Maintenance Zone'), max_length=500 , choices=CHOICE3,null=True)
    Description = models.TextField()
    #meet_date = models.DateTimeField(verbose_name='Fije su cita de inspección técnica',null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,unique=False)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de solicitud',null=True)
    

    

    class Meta:
        ordering = ('-activity',)
        verbose_name = 'Solicitud de Contizacion ProFit'
        verbose_name_plural = 'Solicitudes de Cotizaciones ProFits'

    def __str__(self):
        return 'Cotizacion {}'.format(self.id)




class Visit(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


