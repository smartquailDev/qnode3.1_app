from decimal import Decimal
from django.conf import settings
from edificio_0.models import Cotizacion


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID_0)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID_0] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products 
        from the database.
        """
        invoice_ids = self.cart.keys()
        # get the product objects and add them to the cart
        invoices = Cotizacion.objects.filter(id__in=invoice_ids)

        cart = self.cart.copy()
        for invoice in invoices:
            cart[str(invoice.id)]['invoice'] = invoice

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item ['quantity'] = item['quantity']
            item['total_price'] = item['price'] * item['quantity']
            item['iva'] = Decimal(item['price'])*(Decimal('12')/Decimal('100'))*int(item['quantity'])
            item['anticipo'] = Decimal(item['anticipo'])
            item['price_anticipo'] = (Decimal(item['total_price'])+Decimal(item['iva']))*item['anticipo']
            item['total_price'] = item['price'] * item['quantity']
            item['total'] = item['total_price']*item['anticipo']
           

            yield item
    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, invoice,quantity=1, anticipo=50,update_anticipo=True):
        """
        Add a product to the cart or update its quantity.
        """
        invoice_id = str(invoice.id)
        if invoice_id not in self.cart:
            self.cart[invoice_id] = {'quantity': int(invoice.quantity),
                                      'price': str(invoice.price),'anticipo': 0}

        if update_anticipo:
            self.cart[invoice_id]['anticipo'] = anticipo
        else:
            self.cart[invoice_id]['anticipo'] += anticipo
            
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, invoice):
        """
        Remove a product from the cart.
        """
        invoice_id = str(invoice.id)
        if invoice_id in self.cart:
            del self.cart[invoice_id]
            self.save()

    def total_price(self):
        return sum(Decimal(item['total_price']) for item in self.cart.values())

  

    def Total(self):
        return self.total_price() + self.subtotal_iva()

    def anticipo_total(self):
        return (Decimal(item['price_anticipo']) for item in self.cart.values())


    def Anticipos(self):
        return sum(Decimal(item['price_anticipo']) for item in self.cart.values())

    def anticipos_final(self):
        return self.Anticipos()/Decimal('100')
        


    def subtotal_iva(self):
        return sum(Decimal(item['iva']) for item in self.cart.values())



    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID_0]
        self.save()
