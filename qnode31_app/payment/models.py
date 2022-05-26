from django.db import models
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator

class Check_Payment(models.Model):

    CHOICE=[('Banco del Pichincha','Banco del Pichincha'),
    ('Banco del Pacifico','Banco del Pacifico'),
    ('Banco del Austro','Banco del Austro'),
    ('Produbanco','Produbanco'),
    ('Mutialista Pichincha','Mutualista Pichincha'),
    ('Banco Internacional','Banco Internacional'),
    ('Banco de Guayaquil','Banco de Guayaquil'),
    ('Banco  Bolivariano','Banco Bolivariano'),
    ]
    
    Nombre_banco= models.CharField(max_length=200, db_index=True, choices=CHOICE,verbose_name='Nombre de entidad bancaria',null=True)
    Numero_de_control= models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100000000)],verbose_name='Numero de Control')
    Numero_de_cheque = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(10000000)],verbose_name='Numero de Cheque')
    fecha_de_emision = models.DateTimeField(verbose_name='Fecha de emisón')
    valor = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Valor inscripto',null=True)
    direccion_de_retiro = models.CharField(max_length=200,verbose_name='Dirección de retiro',null=True)


    class Meta:
        ordering=('-fecha_de_emision',)
        verbose_name = 'Pago con chequera'
        verbose_name_plural = 'Pagos con chequera'
        
    def __str__(self):
        return 'pay_check{}'.format(self.id)

class Trans_Payment(models.Model):
  
    transferencia= models.FileField(upload_to='documents/%Y/%m/%d')
   
    class Meta:
        verbose_name = 'Pagos de Trasferencia'
        verbose_name_plural = 'Pagos de Trasferencia'
        
    def __str__(self):
        return 'pay_trans{}'.format(self.id)