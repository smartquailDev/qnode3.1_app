from decimal import Decimal
from django.conf import settings
from edificio_2.models import Cotizacion, Coti_Order


class Cart_Pay(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_PAY_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_PAY_SESSION_ID] = {}
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
            item['price1'] = Decimal(item['price1'])

            yield item
    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, invoice, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        invoice_id = str(invoice.id)
        if invoice_id not in self.cart:
            self.cart[invoice_id] = {'quantity': 0,
                                       'price1': str(invoice.price1)}
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
        return sum(Decimal(item['price1']) for item in self.cart.values())



  

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_PAY_SESSION_ID]
        self.save()
