from django.db import models
from django.urls import reverse
#from parler.models import TranslatableModel, TranslatedFields
from django.contrib.auth.models import User
from ProFit.models import Profile
from decimal import Decimal



class mantenimiento(models.Model):
    CHOICE=[('Correctivo','PMC'),
    ('Preventivo','PMP'),
    ('Correctivo Sistema de Emergencia','PCSE'),
    ('Correctivo Sistema de Revestimientos','PCSR'),
    ]
 
    name = models.CharField(max_length=200,db_index=True,verbose_name='Tipo de Mantenimiento',choices=CHOICE,null=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True,null=True)
       
    class Meta:
        ordering = ('name',)
        verbose_name = 'Tipo de Mantenimiento'
        verbose_name_plural = 'Tipo de Mantenimientos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('Proyectos:product_list_by_category',
                           args=[self.slug])


class Project(models.Model):

    CHOICE=[('Home Detail','Home Detail'),
    ('Habitad','Habitad'),
    ]
    CHOICE2=[('m2','m2'),
    ('m3','m3'),
    ('ml','ml'),
    ('Gl','Gl'),
    ]
    
    Admin_name = models.CharField(max_length=200, db_index=True, choices=CHOICE,verbose_name='Nombre de Aliado',null=True)
    name = models.CharField(max_length=200, db_index=True ,verbose_name='Nombre de Proyecto')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,unique=False)
    direccion = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,unique=False)
    code2= models.CharField(max_length=500,blank=True,verbose_name='Codigo de Proyecto')
    description = models.TextField(blank=True,verbose_name='Descripción de Proyecto')
    category = models.ForeignKey(mantenimiento,related_name='proyecto',on_delete=models.CASCADE,verbose_name='Categoría de Mantenimiento')
    image = models.ImageField(upload_to='proyectos/%Y/%m/%d',blank=True,verbose_name='Imagenes Reportadas')
    slug = models.SlugField(max_length=200, db_index=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Valor Unitario')
    quantity = models.PositiveIntegerField(default=1,verbose_name='Cantidad')
    units = models.CharField(max_length=200, db_index=True, choices=CHOICE2,verbose_name='Unidades',null=True)
    available = models.BooleanField(default=True,verbose_name='Aprobado?')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación de proyecto')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de última actualización de proyecto')
    updated_a = models.DateTimeField(auto_now=True,verbose_name='Fecha de última actualización de anticipo')
    anticipo = models.PositiveIntegerField(default=50,verbose_name='Anticipo')
    

    class Meta:
        verbose_name = 'Proyectos para Aliados'
        verbose_name_plural = 'Proyecto para Aliados'
        index_together = (('id','slug'),)

    def subtotal(self):
        return (self.price * self.quantity)


    def SubTotal_cost(self):
        return ((self.anticipo / Decimal('100')))*self.subtotal()

    def Saldo(self):
        return (self.subtotal()-self.SubTotal_cost())
    



        
    
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('Proyectos:product_detail',args=[self.id, self.slug])