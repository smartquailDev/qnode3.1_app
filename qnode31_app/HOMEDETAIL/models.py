
import uuid
from django.db import models
from decimal import Decimal
from django.utils.html import format_html
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models import F,Value,Count,Avg, Sum, Min, Max, DateTimeField
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
import datetime
from Proyectos.models import Project
from ProFit.models import Profile
#from moneyfield import MoneyField
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
#from django_model_changes import ChangesMixin

#signal used for is_active=False to is_active=True

class Edificios(TranslatableModel):


    CHOICE=[('PFE','PFE'),
        ('PFC','PFC'),
        ('PFU','PFU'),
        ('PFS','PFS'),
        ('PFP','PFP'),
        ]

    translations = TranslatedFields(

        building_code = models.CharField(_('Building Code'),max_length=3,choices=CHOICE),
        building_id = models.CharField(_('Building ID'),max_length=500),
        building_name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
        city = models.CharField(_('city'), max_length=100),
        building_levels = models.IntegerField(default=0, validators=[MaxValueValidator(99)],null=True),
        building_address = models.CharField(_('Building address'), max_length=250),
        building_ruc = models.PositiveIntegerField(null=True,validators=[MaxValueValidator(999999999999999)]),
        building_accountant = models.CharField(_('Building Accountant '), max_length=20),
        insurance_carrier =models.CharField(_('Building insurance carrier '), max_length=20),
        administration_manager = models.CharField(_('administration manager name'), max_length=20),
        manager_administrator_name = models.CharField(_('Manager administrator name'), max_length=50),
        administrator_email = models.EmailField(_('administrator e-mail')),
        administrator_phonenumber = PhoneField(_('administrator phonenumber'),blank=True),
        created = models.DateTimeField(auto_now_add=True,null=True),
        updated = models.DateTimeField(auto_now=True,null=True),
        code= models.CharField(_('codigo'), max_length=50,blank=True),
        project_number= models.CharField(_('Projects Numbers'), max_length=50,blank=True),
    )
    aprobar = models.BooleanField(null=True)


class Meta:
    verbose_name = 'Información del Edificio'
    verbose_name_plural = 'Datos del Edificio'

    def __str__(string):
        return 'Edificio: {}'.format(self.code)

    def __str__(self):
        return self.building_name

@property
def Codigo(self):
        return ' '.join([self.building_code,' ',self.building_id,' '])

def save(self):
    self.code = self.Codigo
    super(Edificios,self).save()











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

class Analitycs(models.Model):
    CHOICES=[('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ]


    projectPM = models.ForeignKey(Proyecto,related_name='items',on_delete=models.CASCADE)
   # invoice_PM = models.ForeignKey(CotizacionPM,related_name='cotipm',on_delete=models.CASCADE)
    items = models.CharField(null=True,max_length=2,choices=CHOICES)
    price1 = models.DecimalField(_('Promain workhand Price'),max_digits=10, decimal_places=2)
    porce = models.DecimalField(_('feed Promain WorkHand'),max_digits=3, decimal_places=2)
    total2 = models.CharField(null=True,max_length=2)



    @property
    def Value(self):
        return self.price1 * self.porce

    def save(self):
        self.total2 = self.Value
        super (Analitycs2, self).save()


    def __str__(self):
        return '{}'.format(self.id)



    def get_cost(self):
        return self.price1 * self.porce

    class Meta:
        verbose_name = 'Análisis de Costo Mano de Obra'
        verbose_name_plural = 'Análisis de Costos Mano de Obra'

class Analitycs2(models.Model):
    CHOICES=[('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ]

    project = models.ForeignKey(Proyecto,null=True,related_name='items2',on_delete=models.CASCADE)
    #invoice_PM = models.ForeignKey(CotizacionPM,null=True,related_name='cotipm2',on_delete=models.CASCADE)
    items = models.CharField(max_length=2,null=True,choices=CHOICES)
    price2 = models.DecimalField(_('ProTools Materials Price'),max_digits=10, decimal_places=2)
    porce2 = models.DecimalField(_('feed Protools Materials'),max_digits=3, decimal_places=2)
    total1 = models.CharField(null=True,max_length=2)

    @property
    def Value(self):
        return self.price2 * self.porce2

    def save(self):
        self.total1 = self.Value
        super (Analitycs, self).save()



    def __str__(self):
        return '{}'.format(self.id)



    def get_cost2(self):
        return self.price1 * self.porce2

    class Meta:
        verbose_name = 'Análisis de Costo Materiales'
        verbose_name_plural = 'Análisis de Costos Materiales'

class PlandeTrabajo(models.Model):
    CHOICES=[('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ]


    project2 = models.ForeignKey(Project,null=True,related_name='items3',on_delete=models.CASCADE)
    items = models.CharField(max_length=2,null=True,choices=CHOICES)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total = models.DateTimeField(null=True)


    @property
    def Fecha(self):
        return self.start_time - self.end_time

    def Value(self):
        self.total = self.Value
        super (PlandeTrabajo, self).save()


    def __str__(self):
        return '{}'.format(self.id)



    def get_cost3(self):
        return self.start_time - self.end_time

    class Meta:
        verbose_name = 'Plan de Trabajo'
        verbose_name_plural = 'Planes de Trabajo'

class Diagnostico(TranslatableModel):


    CHOICE=[('RMC','RMC'),
        ('RMP','RMP'),
        ('RSE','RSE'),
        ('RSR','RSR'),
        ]

    translations = TranslatedFields(

        #Edificio =models.ForeignKey(Edificios,related_name='Edificios3',on_delete=models.CASCADE,null=True,verbose_name='Edificios HomeDetail'),
        report_code = models.CharField(_('Report Code'),max_length=3,choices=CHOICE),
        report_id = models.CharField(_('Report ID'),max_length=2),
        created = models.DateTimeField(_('Date report Created'),auto_now_add=True,null=True),
        date_meet = models.DateTimeField(_('Date Technical meet'),null=True),
        project_name2 = models.CharField(_('Project name'), max_length=50,help_text='Escribir Nombre de Proyecto'),

        item_name = models.CharField(_('item Name'),max_length=20,null=True,blank=True),
        item_description =models.TextField(_('Item description'),null=True,blank=True),
        image_item = models.ImageField(_('image Item'),null=True, blank=True, upload_to="static/edificios/"),

        item_name2 = models.CharField(_('item Name'),max_length=20,null=True,blank=True),
        item_description2 =models.TextField(_('Item description'),null=True,blank=True),
        image_item2 = models.ImageField(_('image Item'),null=True, blank=True, upload_to="static/edificios/"),

        item_name3 = models.CharField(_('item Name'),max_length=20,null=True,blank=True),
        item_description3 =models.TextField(_('Item description'),null=True,blank=True),
        image_item3 = models.ImageField(_('image Item'),null=True, blank=True, upload_to="static/edificios/"),

        promain_code = models.CharField(_('ProMain Code'),max_length=20,help_text='Codigo de Tecnico Profix Responsable'),
        dayswork = models.IntegerField(_('Calendary days'),default=0, validators=[MaxValueValidator(15)],null=True),
        code= models.CharField(_('codigo'), max_length=10,blank=True)
    )


    class Meta:
        verbose_name = 'Diagnostico de Mantenimiento'
        verbose_name_plural = 'Diagnostico de Mantenimiento'

    def __str__(self):
        return 'Reporte: {}'.format(self.code)

    @property
    def Codigo(self):
        return ' '.join([self.report_code,' ',self.report_id,' ',])


    def save(self):
        self.code = self.Codigo
        super (Diagnostico, self).save()


class Cotizacion(models.Model):

    CHOICE2=[('CMC','CMC'),
    ('CMP','CMP'),
    ('CSE','CSE'),
    ('CSR','CSR'),
    ]

    coti_code = models.CharField(max_length=3,choices=CHOICE2,null=True)
    project_name =models.ForeignKey(Project,related_name='project',on_delete=models.CASCADE,null=True)
    Edificio =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    report_code= models.ForeignKey(Diagnostico,related_name='project',on_delete=models.CASCADE,null=True)
    email = models.EmailField(null=True)
    dire= models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False,verbose_name='Aprobado')
    paid2 = models.BooleanField(default=False,verbose_name='Rechazado')
    iva= models.IntegerField(default=12,validators=[MinValueValidator(0),MaxValueValidator(100)])
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


    def __str__(self):
        return 'Cotización {}'.format(self.id)

    #def __str__(self):
        #return '{}'.format(self.first_name)


    def __bool__(self):
        return self.paid

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))

    def get_total_tax_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        total_tax_cost = total_cost * (self.iva / Decimal('100'))
        return total_tax_cost

    def get_total(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        total_tax_cost = total_cost * (self.iva / Decimal('100'))
        total = total_tax_cost + total_cost
        return total

    @property
    def Codigo(self):
        return ' '.join([self.coti_code,' ','{}'.format(self.id),' ',])

    def save(self):
        self.code = self.Codigo
        super (Cotizacion, self).save()





class InvoiceItem(models.Model):
    UNITS=[('mL','ml'),
    ('m^2','m^2'),
    ('Kg','Kg'),
    ('Gl','Gl'),
    ]


    cotizacion = models.ForeignKey(Cotizacion,
                              related_name='items',
                              on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='project_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    Unit = models.CharField(max_length=3,choices=UNITS,null=True)

    def __str__(self):
          return '{}'.format(self.id)



    def get_cost(self):
        return self.price * self.quantity






class Facturacion(TranslatableModel):


    BANCO=[('Pichincha','Pichincha'),
        ('Produbanco','Produbanco'),
        ('Banco de Guayaquil','Banco de Guayaquil'),
        ('Banco Internacional','Banco Internacional'),
        ]

    translations = TranslatedFields(

        Edificio =models.ForeignKey(Edificios,related_name='Edificios2',on_delete=models.CASCADE,null=True,verbose_name='Edificios HomeDetail'),
        Egreso_num = models.CharField(_('Numero de Egreso'),max_length=200,null=True),
        project_name =models.ForeignKey(Project,related_name='projectName',on_delete=models.CASCADE,null=True),
        cotizacion = models.ForeignKey(Cotizacion,on_delete=models.CASCADE,null=True),
        created = models.DateTimeField(_('Date report Created'),auto_now_add=True,null=True),
        EgresoHD  = models.FileField(upload_to='Egreso_HomeDetail/'),
        numero_cheque=models.DecimalField(max_digits=5, decimal_places=2,null=True,verbose_name='NUmeracion de cheque'),
        banco = models.CharField(max_length=55,null=True,choices=BANCO,verbose_name='Entidad Bancaria'),
        #valor_egreso = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',verbose_name='Valor de Egreso'),
        #valor_retencion = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',verbose_name='Valor de Retencion'),
        Aprobado = models.BooleanField(default=False),
        Anuluado = models.BooleanField(default=False)

            )



    class Meta:
        verbose_name = 'Notas de Egreso Home Detail'
        verbose_name_plural = 'Notas de Egreso Home Detail'

    def __str__(self):
        return 'Numero de egreso: {}'.format(self.Egreso_num)
