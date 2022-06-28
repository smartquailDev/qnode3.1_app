from decimal import Decimal
from django.conf import settings
from edificio_2.models import Coti_Order


class Cart_Pay(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart_pay = self.session.get(settings.CART_PAY_SESSION_ID)
        if not cart_pay:
            # save an empty cart in the session
            cart_pay = self.session[settings.CART_PAY_SESSION_ID] = {}
        self.cart_pay = cart_pay

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products 
        from the database.
        """
        project_invoice_ids = self.cart_pay.keys()
        # get the product objects and add them to the cart
        project_invoices = Coti_Order.objects.filter(id__in=project_invoice_ids)

        cart_pay = self.cart_pay.copy()
        for project_invoice in project_invoices:
            cart_pay[str(project_invoice.id)]['project_invoice'] = project_invoice

        for item in cart_pay.values():
            item['total'] = Decimal(item['total'])
            item['total_tax'] = Decimal(item['total'])*(Decimal('12')/Decimal('100'))
            item['total_cost'] = item['total_tax'] + item['total']
            yield item
    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['date'] for item in self.cart_pay.values())

    def add(self, project_invoice, date=True, update_date=False):
        """
        Add a product to the cart or update its quantity.
        """
        project_invoice_id = str(project_invoice.id)
        if project_invoice_id not in self.cart:
            self.cart_pay[project_invoice_id] = {'date': str(project_invoice.date)}
        if update_date:
            self.cart_pay[project_invoice_id]['date'] = date
        else:
            self.cart_pay[project_invoice_id]['date'] += date
        
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, project_invoice):
        """
        Remove a product from the cart.
        """
        project_invoice_id = str(project_invoice.id)
        if project_invoice_id in self.cart_pay:
            del self.cart_pay[project_invoice_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_PAY_SESSION_ID]
        self.save()
