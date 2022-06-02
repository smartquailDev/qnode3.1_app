from decimal import Decimal
from django.conf import settings
from .models import Cotizacion
#from coupons.models import Coupon
from django.db.models import Count, F, Value


class Coti_Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        coti_cart = self.session.get(settings.COTI_CART_SESSION_ID)
        if not coti_cart:
            # save an empty cart in the session
            coti_cart = self.session[settings.COTI_CART_SESSION_ID] = {}
        self.coti_cart = coti_cart
        #Systema de cupones de descuento
        #self.coupon_id = self.session.get('coupon_id')
    
       

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products 
        from the database.
        """
        invoice_ids = self.coti_cart.keys()
        # get the product objects and add them to the cart
        invoices = Cotizacion.objects.filter(id__in=invoice_ids)

        coti_cart = self.coti_cart.copy()
        for invoice in invoices:
            coti_cart[str(invoice.id)]['invoice'] = invoice

        for item in coti_cart.values():
            item['price'] = Decimal(item['price'])
            item['anticipo'] = Decimal(item['anticipo'])/Decimal('10')
            item['total_price'] = item['price'] * item['quantity']*item['anticipo']
            item['total'] = item['total_price']*item['anticipo']
            yield item

    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.coti_cart.values())

    def add(self, invoice, quantity=1, anticipo=50, update_quantity=False,update_anticipo=False):
        """
        Add a product to the cart or update its quantity.
        """
        invoice_id = str(invoice.id)
        if invoice_id not in self.coti_cart:
            self.coti_cart[invoice_id] = {'quantity': 0,'price': str(invoice.price),'anticipo': 0}
        if update_quantity:
            self.coti_cart[invoice_id]['quantity'] = quantity
        else:
            self.coti_cart[invoice_id]['quantity'] += quantity

        if update_anticipo:
            self.coti_cart[invoice_id]['anticipo'] = anticipo
        else:
            self.coti_cart[invoice_id]['anticipo'] += anticipo
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, invoice):
        """
        Remove a product from the cart.
        """
        invoice_id = str(invoice.id)
        if invoice_id in self.coti_cart:
            del self.coti_cart[invoice_id]
            self.save()

    def get_total_price(self):
        return sum((Decimal(item['total_price'])) for item in self.coti_cart.values())

    def Sub_total_price(self):
        return (self.get_total_price()*sum(item['anticipo'] for item in self.coti_cart.values()) )

    def Anticipos(self):
        return sum(Decimal(item['anticipo']) for item in self.coti_cart.values())
        
    def Sub_total(self):
        return sum(Decimal(item['price'])*item['quantity']for item in self.coti_cart.values())

    def total(self):
        return self.Anticipos()*self.get_total_price()

    def total2(self):
        return sum((Decimal(item['total_price'])) for item in self.coti_cart.values())

    #def get_total_price_2(self):
        #return self.get_total_price() - self.Anticipos()


    def clear(self):
        # remove cart from session
        del self.session[settings.COTI_CART_SESSION_ID]
        self.save()
    
    
  


  

    

    
