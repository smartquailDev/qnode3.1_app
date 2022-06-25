from decimal import Decimal
from django.conf import settings
from edificio_2.models import Coti_Order


class Cart_Pay(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products 
        from the database.
        """
        invoice_ids = self.cart.keys()
        # get the product objects and add them to the cart
        invoices = Coti_Order.objects.filter(id__in=invoice_ids)

        cart = self.cart.copy()
        for invoice in invoices:
            cart[str(invoice.id)]['invoice'] = invoice

        for item in cart.values():
            item['total'] = Decimal(item['total'])
            item['total_tax'] = Decimal(item['total'])*(Decimal('12')/Decimal('100'))
            item['total_cost'] = item['total_tax'] + item['total']
            yield item
    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, invoice, quantity=1, update_quantity=False,update_anticipo=True):
        """
        Add a product to the cart or update its quantity.
        """
        invoice_id = str(invoice.id)
        if invoice_id not in self.cart:
            self.cart[invoice_id] = {'quantity': 0,
                                      'price': str(invoice.price)}
        if update_quantity:
            self.cart[invoice_id]['quantity'] = quantity
        else:
            self.cart[invoice_id]['quantity'] += quantity
        
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

    def get_total_price(self):
        return sum((Decimal(item['total'])) for item in self.cart.values())

    def Sub_total_price(self):
        return (self.get_total_price()*sum(item['anticipo'] for item in self.cart.values()) )

    def Anticipos(self):
        return sum(Decimal(item['anticipo']) for item in self.cart.values())
        
    def Sub_total(self):
        return sum(Decimal(item['price'])*item['quantity']for item in self.cart.values())

    def subtotal_iva(self):
        return sum(Decimal(item['iva']) for item in self.cart.values())

    def total(self):
        return self.Sub_total() + self.subtotal_iva()

    def total_anticipo(self):
        return self.total()*self.Anticipos()
    
    def total_pendiente(self):
        return self.total() - self.total_anticipo()

    def total2(self):
        return sum((Decimal(item['total_price'])) for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
