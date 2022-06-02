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
#from django.contrib.auth.models import User
from django.urls import reverse

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
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,unique=False)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de solicitud',null=True)
    visit = models.DateTimeField(verbose_name='visita técnica',null=True)
    
    class Meta:
        ordering = ('-activity',)
        verbose_name = 'Solicitud de Contizacion ProFit'
        verbose_name_plural = 'Solicitudes de Cotizaciones ProFits'

    def __str__(self):
        return 'Cotizacion {}'.format(self.id)

class Diagnostico(TranslatableModel):


    CHOICE=[('RMC','RMC'),
        ('RMP','RMP'),
        ('RSE','RSE'),
        ('RSR','RSR'),
        ]

    UNITS=[('mL','ml'),
    ('m^2','m^2'),
    ('Kg','Kg'),
    ('Gl','Gl'),
    ]

    translations = TranslatedFields(

        #Edificio =models.ForeignKey(Edificios,related_name='Edificios3',on_delete=models.CASCADE,null=True,verbose_name='Edificios HomeDetail'),
        report_code = models.CharField(_('Report Code'),max_length=3,choices=CHOICE),
        report_id = models.CharField(_('Report ID'),max_length=2),
        created = models.DateTimeField(_('Date report Created'),auto_now_add=True,null=True),
        date_meet = models.DateTimeField(_('Date Technical meet'),null=True),
        project_name2 = models.CharField(_('Project name'), max_length=50,help_text='Escribir Nombre de Proyecto'),
       

        # item_name = models.CharField(_('item Name'),max_length=20,null=True,blank=True),
        item_description =models.TextField(_('Item description'),null=True,blank=True),
        image_item = models.ImageField(_('image Item'),null=True, blank=True, upload_to="static/edificios/"),
        price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Costo Unitario'),
        quantity = models.PositiveIntegerField(default=1,null=True,blank=True,verbose_name= 'Cantidad'),
        Unit = models.CharField(max_length=3,choices=UNITS,null=True,blank=True,verbose_name= 'Unidades'),
        iva= models.IntegerField(default=12,validators=[MinValueValidator(0),MaxValueValidator(100)]),

        promain_code = models.CharField(_('ProMain Code'),max_length=20,help_text='Codigo de Tecnico Profix Responsable'),
        dayswork = models.IntegerField(_('Calendary days'),default=0, validators=[MaxValueValidator(15)],null=True),
        code= models.CharField(_('codigo'), max_length=10,blank=True)
    )


    class Meta:
        verbose_name = 'Diagnostico de Mantenimiento'
        verbose_name_plural = 'Diagnostico de Mantenimiento'

    def __str__(self):
        return 'Reporte: {}'.format(self.code)

    def sub_total(self):
        return '{} $' .format(self.price * self.quantity)

    def total(self):
        return '{} $' .format((self.price * self.quantity) + ((self.iva / Decimal('100')) * self.price * self.quantity))

    @property
    def Codigo(self):
        return ' '.join([self.report_code,' ',self.report_id,' ',])


    def save(self):
        self.code = self.Codigo
        super (Diagnostico, self).save()




class Category(models.Model):
    
    CHOICE3=[('MC','Mantenimiento Correctivo'),
             ('MP','Mantenimiento Preventivo'),
    ]

    maintenace_type = models.CharField(max_length=200, choices=CHOICE3,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('maintenace_type',)
        verbose_name = 'Categoria de Mantenimiento'
        verbose_name_plural = 'Categorias de Mantenimientos'

    def __str__(self):
        return self.maintenace_type

    def get_absolute_url(self):
        return reverse('edificio_1:invoice_list_by_category',args=[self.slug])


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
    project_name =models.ForeignKey(Diagnostico,related_name='project',on_delete=models.CASCADE,null=True,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,null=True)
    Edificio =models.OneToOneField(Profile, on_delete=models.CASCADE ,null=True)
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
        return self.coti_code

    def Sub_total(self):
        return self.price * self.quantity
    
    def Sub_Total_IVA(self):
        total_tax_cost = (self.price * self.quantity) * (self.iva / Decimal('100'))
        return '{} $'.format(total_tax_cost)

    def Total(self):
        total_cost = (self.price * self.quantity) * (self.iva / Decimal('100')) + (self.price * self.quantity)
        return '{} $'.format(total_cost)

    #def __str__(self):
        #return '{}'.format(self.first_name)

    @property
    def Codigo(self):
        return ' '.join([self.coti_code,' ','{}'.format(self.id),' ',])

    def save(self):
        self.code = self.Codigo
        super (Cotizacion, self).save()

    def get_absolute_url(self):
        return reverse('edificio_1:invoice_detail',args=[self.id,self.slug])



class order_cotizacion(models.Model):
    code = models.BigIntegerField(null=True, verbose_name='Escriba su codigo único de aprobación')
    email = models.EmailField(verbose_name='Escriba su correo electrico')
    aprobe= models.BooleanField(default=False, verbose_name='Aprobado')
    diss= models.BooleanField(default=False, verbose_name='rechazado')
    iva= models.IntegerField(default=12,validators=[MinValueValidator(0),MaxValueValidator(100)])
    discount = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])

    class Meta:
        ordering = ('-email',)

    def __str__(self):
        return  'Cotización {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __bool__(self):
        return self.paid

    def Sub_Total(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return '{} $'.format(total_cost - total_cost * (self.discount / Decimal('100')))

    def Sub_Total_IVA(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        total_tax_cost = total_cost * (self.iva / Decimal('100'))
        return '{} $'.format(total_tax_cost)

    def Total(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        total_tax_cost = total_cost * (self.iva / Decimal('100'))
        total = total_tax_cost + total_cost
        return '{} $'.format(total)



class InvoiceItem(models.Model):
    UNITS=[('mL','ml'),
    ('m^2','m^2'),
    ('Kg','Kg'),
    ('Gl','Gl'),
    ]
    order = models.ForeignKey(order_cotizacion, related_name='items', on_delete=models.CASCADE,null=True)
    coti = models.ForeignKey(Cotizacion,
                              related_name='order_items',
                              on_delete=models.CASCADE)
    invoice = models.ForeignKey(Diagnostico,related_name='invoice_items',on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity = models.PositiveIntegerField(default=1)
    Unit = models.CharField(max_length=3,choices=UNITS,null=True)

    def __str__(self):
          return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Proyecto(models.Model):
    project_name = models.CharField(max_length=3,null=True,verbose_name='Codigo de Proyecto')
    invoice_code = models.CharField(max_length=3,null=True,verbose_name='Codigo de Cotización')
    created = models.DateTimeField(auto_now_add=True,null=True,verbose_name='Fecha de Creación')
    Fecha = models.DateField(null=True,verbose_name='Fecha de entrega de Proyecto')
    porcet2=models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name='Avance de Obra %')
    porcet=models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name='Porcetanje de Anticipo %')
    value2= models.DecimalField(max_digits=10, decimal_places=2,null=True,verbose_name='Valor neto de la cotización')
    value3=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    value4=models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def Avance_de_Obra(self):
        if self.porcet2:
            percentage2 = round((self.porcet2), 0)
        else:
                percentage2 = 0
        return format_html(
        """
        <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
        """,
            percentage2 )


    @property
    def Advance(self):
        if self.porcet and self.value2:
            advance2 =  round((self.porcet/100) * self.value2,2)
        else:
            advance2=0
        return  advance2

    @property
    def Saldo_a_cancelar(self):
        if self.Advance and self.value2:
            saldo =  round((self.value2) - (self.Advance),2)
        else:
            saldo=0
        return  saldo



    def Anticipo(self):
        if self.value2 and self.Advance:
            percentage = round((self.Advance / self.value2*100 ), 0)
        else:
            percentage = 0

        return format_html(
                """
                <progress value="{0}" max="100"></progress>
                <span style="font-weight:bold">{0}%</span>
                """,
                percentage )



    def save(self):
        self.value3 = self.Advance
        self.value4 = self.Saldo_a_cancelar
        super(Proyecto, self).save()

    class Meta:
        verbose_name = 'Seguimiento de Proyecto'
        verbose_name_plural = 'Seguimiento de Proyecto'

class ProyectosHomeDetail(Proyecto): #Extends funcs of model without creating a table in DB
    class Meta:
        proxy = True
        verbose_name = 'Seguimiento de Proyecto'
        verbose_name_plural = 'Seguimiento de Proyecto'



class Visit(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
