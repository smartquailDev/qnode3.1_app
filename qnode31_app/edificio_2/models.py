from statistics import quantiles
from tabnanny import verbose
#from tkinter import CASCADE
from django.db import models
from django import forms
from decimal import Decimal
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ProFit.models import Profile
from django.utils.html import format_html
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.safestring import mark_safe
import time
from datetime import datetime, timedelta
from django.contrib.auth.models import Group

class Category(models.Model):
    
    CHOICE3=[('Correctivo','MC'),
             ('Preventivo','MP'),
    ]

    name = models.CharField(max_length=200, choices=CHOICE3,db_index=True,verbose_name='Tipo de mantenimiento')
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categoria de Mantenimiento'
        verbose_name_plural = 'Categorias de Mantenimientos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('edificio_2:invoice_list_by_category',args=[self.slug])

class Cotizacion(models.Model):

    CHOICE2=[('CMC','CMC'),
    ('CMP','CMP'),
    ('CSE','CSE'),
    ('CSR','CSR'),
    ]

    UNITS=[('mL','ml'),
    ('m^2','m^2'),
    ('Kg','Kg'),
    ('Gl','Gl'),
    ]

    coti_code = models.CharField(max_length=3,choices=CHOICE2,null=True)
    category = models.ForeignKey(Category, related_name='invoices',on_delete=models.CASCADE,verbose_name='Categoria de Mantenimiento',null=True)
    #project_name =models.ForeignKey(Diagnostico,related_name='project',on_delete=models.CASCADE,null=True,db_index=True)
    name = models.CharField(max_length=1000000,blank=True, null=True,verbose_name='Nombre de Proyecto',db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,null=True)
    #Edificio =models.OneToOneField(Profile, on_delete=models.CASCADE ,null=True)
    item =  models.CharField(max_length=1000,blank=True)
    description = models.CharField(max_length=1000000,blank=True, null=True)
    Units = models.CharField(max_length=3,choices=UNITS,null=True)
    image = models.ImageField(upload_to='image_item/%Y/%m/%d',blank=True,verbose_name='Imagenes Reportadas')
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True,verbose_name='Disponible')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Valor Unitario',null=True)
    iva= models.IntegerField(default=12,validators=[MinValueValidator(0),MaxValueValidator(100)])
    quantity = models.PositiveIntegerField(default=1,null=True)
    updated_a = models.DateTimeField(auto_now=True,verbose_name='Fecha de última actualización de anticipo',null=True)
    anticipo = models.PositiveIntegerField(default=50,verbose_name='Anticipo',null=True)
    #coupon = models.ForeignKey(Coupon,
                               #related_name='projects',
                               #null=True,
                               #blank=True,
                               #on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    code= models.CharField(max_length=1000000,blank=True)

    class Meta:
        verbose_name = 'la Cotización de Proyectos'
        verbose_name_plural = 'Cotización de Proyectos'
        ordering = ('-created',)
        index_together = (('id','slug'),)


    def __str__(self):
        return self.name

    def Sub_total(self):
        return self.price * self.quantity
    
    def Sub_Total_IVA(self):
        total_tax_cost = (self.price * self.quantity) * (self.iva / Decimal('100'))
        return total_tax_cost

    def Total(self):
        total_cost = (self.price * self.quantity) * (self.iva / Decimal('100')) + (self.price * self.quantity)
        return total_cost

    #def __str__(self):
        #return '{}'.format(self.first_name)

    @property
    def Codigo(self):
        return ' '.join([self.coti_code,' ','{}'.format(self.id),' ',])

    def save(self):
        self.code = self.Codigo
        super (Cotizacion, self).save()

    def get_absolute_url(self):
        return reverse('edificio_2:invoice_detail',args=[self.id,self.slug])


class Coti_Order(models.Model):

    CHOICE2=[('CMC','CMC'),
    ('CMP','CMP'),
    ('CSE','CSE'),
    ('CSR','CSR'),
    ]
    coti_code = models.CharField(max_length=3,choices=CHOICE2,null=True)
    building_name =  models.ForeignKey(Group, on_delete=models.CASCADE,null=True,unique=False)
    slug = models.SlugField(max_length=200,db_index=True,null=True)
   # nombre= models.CharField(_('Nombre de Edificio'), max_length=50,null=True)
    user_name =  models.ForeignKey(User, on_delete=models.CASCADE,null=True,unique=False)
    coti = models.ForeignKey(Cotizacion, on_delete=models.CASCADE,null=True,unique=False)
    category= models.ForeignKey(Category, on_delete=models.CASCADE,null=True,unique=False)
    email = models.EmailField(_('Correo Electrónico'))
   # address = models.CharField(_('Dirección'), max_length=250)
    RUC2 = models.CharField(_('RUC'), max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    aprobe = models.BooleanField(default=True)

   # braintree_id = models.CharField(max_length=150, blank=True)
   # coupon = models.ForeignKey(Coupon,
    #                           related_name='orders',
    #                           null=True,
    #                           blank=True,
    #                           on_delete=models.SET_NULL)
    
    
    dias = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(300)])
    date = models.DateTimeField(null=True,blank=True)
    price1 = models.DecimalField(max_digits=1000, decimal_places=2,null=True,verbose_name='Valor total de Cotización')
    price2 = models.DecimalField(max_digits=10000, decimal_places=2,null=True)
    price3 = models.DecimalField(max_digits=10000, decimal_places=2,null=True)

    Iva2 = models.PositiveSmallIntegerField(default=12)
    code= models.CharField(max_length=1000000,blank=True)
  #  coti2 = models.ManyToManyField(to='HOMEDETAIL.Cotizacion')

    
   

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Ordenes de Compras'
        index_together = (('id','slug'),)

    @property
    def Codigo(self):
        return ' '.join([self.coti_code,' ','{}'.format(self.id),' ',])

  

    def save(self):
        self.code = self.Codigo
        super (Coti_Order, self).save()

    def __str__(self):
        return 'Order {}'.format(self.id)

    def coti_order_pdf(obj):
        return mark_safe('<a href="{}"><i class="fa fa-file"></i></a>'.format(
            reverse('edificio_2:admin_coti_order_pdf', args=[obj.id])))
        coti_order_pdf.short_description = 'Invoice'

    #def __str__(self):
        #return '{}'.format(self.first_name)

    def exp_date(self):
        timedifer = self.created + timedelta(days=14)
        return timedifer


    def __bool__(self):
        return self.aprobe

    def iva_price(self):
        iva = self.Iva2/Decimal('100')
        return iva

    def get_total_cost(self):
        total_cost = sum(item.get_cost()*item.Anticipo() for item in self.items.all())
        return total_cost

    def total(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost

    def total_tax(self):
        total_tax = self.total()*self.iva_price()
        return total_tax

    def TOTAL(self):
        total_cost = self.total_tax() + self.total()
        return total_cost

    def anticipo_cost(self):
        anticpo_cost = sum(item.get_cost_anticipo() for item in self.items.all())
        return anticpo_cost
    
    def anticipo_cost_tax(self):
        anticpo_cost_tax = self.anticipo_cost()*self.iva_price()
        return anticpo_cost_tax

    def anticipo_tota_cost_tax(self):
        anticpo_total_cost_tax = self.anticipo_cost_tax()+ self.anticipo_cost()
        return anticpo_total_cost_tax

    def pendiente(self):
        pago_pendiente = self.TOTAL()-self.anticipo_tota_cost_tax()
        return pago_pendiente 

    def get_absolute_url(self):
        return reverse('edificio_2:project_detail',args=[self.id,self.slug])


class Coti_OrderItem(models.Model):
    order = models.ForeignKey(Coti_Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    invoice = models.ForeignKey(Cotizacion,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    anticipo = models.PositiveIntegerField(default=50,verbose_name='anticipo')

    def Anticipo(self):
        return self.anticipo / Decimal('10')



    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def get_cost_anticipo(self):
        return self.get_cost()*self.Anticipo() 


class Project_Order(models.Model):

    CHOICE2=[('CMC','CMC'),
    ('CMP','CMP'),
    ('CSE','CSE'),
    ('CSR','CSR'),
    ]
    project_code = models.CharField(max_length=3,choices=CHOICE2,null=True)
    building_name =  models.ForeignKey(Group, on_delete=models.CASCADE,null=True,unique=False)
    slug = models.SlugField(max_length=200,db_index=True,null=True)
   # nombre= models.CharField(_('Nombre de Edificio'), max_length=50,null=True)
    user_name =  models.ForeignKey(User, on_delete=models.CASCADE,null=True,unique=False)
    coti = models.ForeignKey(Cotizacion, on_delete=models.CASCADE,null=True,unique=False)
    category= models.ForeignKey(Category, on_delete=models.CASCADE,null=True,unique=False)
    email = models.EmailField(_('Correo Electrónico'))
   # address = models.CharField(_('Dirección'), max_length=250)
    RUC2 = models.CharField(_('RUC'), max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    aprobe = models.BooleanField(default=True)

   # braintree_id = models.CharField(max_length=150, blank=True)
   # coupon = models.ForeignKey(Coupon,
    #                           related_name='orders',
    #                           null=True,
    #                           blank=True,
    #                           on_delete=models.SET_NULL)
    
    
    dias = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(300)])
    date = models.DateTimeField(null=True,blank=True)
 

    Iva2 = models.PositiveSmallIntegerField(default=12)
    code= models.CharField(max_length=1000000,blank=True)
  #  coti2 = models.ManyToManyField(to='HOMEDETAIL.Cotizacion')

    
   

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Proyectos'
        verbose_name_plural = 'Proyectos'
        index_together = (('id','slug'),)

    @property
    def Codigo(self):
        return ' '.join([self.project_code,' ','{}'.format(self.id),' ',])

  

    def save(self):
        self.code = self.Codigo
        super (Project_Order, self).save()

    def __str__(self):
        return 'Order {}'.format(self.id)

    def project_order_pdf(obj):
        return mark_safe('<a href="{}"><i class="fa fa-file"></i></a>'.format(
            reverse('edificio_2:admin_project_order_pdf', args=[obj.id])))
        coti_order_pdf.short_description = 'Project_Invoice'

    #def __str__(self):
        #return '{}'.format(self.first_name)

    def exp_date(self):
        timedifer = self.created + timedelta(days=14)
        return timedifer


    def __bool__(self):
        return self.aprobe

    def iva_price(self):
        iva = self.Iva2/Decimal('100')
        return iva

    def get_total_cost(self):
        total_cost = sum(item.get_cost()*item.Anticipo() for item in self.items.all())
        return total_cost

    def total(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost

    def total_tax(self):
        total_tax = self.total()*self.iva_price()
        return total_tax

    def TOTAL(self):
        total_cost = self.total_tax() + self.total()
        return total_cost

    def anticipo_cost(self):
        anticpo_cost = sum(item.get_cost_anticipo() for item in self.items.all())
        return anticpo_cost
    
    def anticipo_cost_tax(self):
        anticpo_cost_tax = self.anticipo_cost()*self.iva_price()
        return anticpo_cost_tax

    def anticipo_tota_cost_tax(self):
        anticpo_total_cost_tax = self.anticipo_cost_tax()+ self.anticipo_cost()
        return anticpo_total_cost_tax

    def pendiente(self):
        pago_pendiente = self.TOTAL()-self.anticipo_tota_cost_tax()
        return pago_pendiente 

    def get_absolute_url(self):
        return reverse('edificio_2:project_detail',args=[self.id,self.slug])


class Project_OrderItem(models.Model):
    order = models.ForeignKey(Project_Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    invoice = models.ForeignKey(Coti_Order,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price1 = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    anticipo = models.PositiveIntegerField(default=50,verbose_name='anticipo')

    def Anticipo(self):
        return self.anticipo / Decimal('10')



    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price1 * self.quantity

    def get_cost_anticipo(self):
        return self.get_cost()*self.Anticipo() 