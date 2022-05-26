from django.db import models
from Proyectos.models import Project
from django import forms
from decimal import Decimal
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from coupons.models import Coupon
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class Order(models.Model):

    building_name =  models.ForeignKey(User, on_delete=models.CASCADE,null=True,unique=False)
    nombre= models.CharField(_('Nombre de Edificio'), max_length=50,null=True)
    admin_name = models.CharField(_('Nombre de Administrador'), max_length=50)
   # coti = models.ForeignKey(Cotizacion, on_delete=models.CASCADE,null=True,unique=False)
    email = models.EmailField(_('Correo Electrónico'))
    address = models.CharField(_('Dirección'), max_length=250)
    RUC2 = models.CharField(_('RUC'), max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    coupon = models.ForeignKey(Coupon,
                               related_name='orders',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    
    
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
  

    Iva2 = models.PositiveSmallIntegerField(default=12)
    coti2 = models.ManyToManyField(to='HOMEDETAIL.Cotizacion')
   

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Ordenes de Compras'

    def __str__(self):
        return 'Order {}'.format(self.id)

    #def __str__(self):
        #return '{}'.format(self.first_name)

    def __str__(self):
        return self.address

    def __bool__(self):
        return self.paid

    def get_total_cost(self):
        total_cost = sum(item.get_cost()*item.Anticipo() for item in self.items.all())
        return total_cost - (total_cost * (self.discount / Decimal('100')))

   


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Project,
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
