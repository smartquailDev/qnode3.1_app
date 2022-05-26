from decimal import Decimal
from django.conf import settings
from Proyectos.models import Project
from coupons.models import Coupon
from django.db.models import Count, F, Value


class Cart(object):

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
        #Systema de cupones de descuento
        self.coupon_id = self.session.get('coupon_id')
    
       

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products 
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Project.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['anticipo'] = Decimal(item['anticipo'])/Decimal('10')
            item['total_price'] = item['price'] * item['quantity']*item['anticipo']
            item['total'] = item['total_price']*item['anticipo']
            yield item

    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, anticipo=50, update_quantity=False,update_anticipo=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,'price': str(product.price),'anticipo': 0}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        if update_anticipo:
            self.cart[product_id]['anticipo'] = anticipo
        else:
            self.cart[product_id]['anticipo'] += anticipo
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum((Decimal(item['total_price'])) for item in self.cart.values())

    def Sub_total_price(self):
        return (self.get_total_price()*sum(item['anticipo'] for item in self.cart.values()) )

    def Anticipos(self):
        return sum(Decimal(item['anticipo']) for item in self.cart.values())
        
    def Sub_total(self):
        return sum(Decimal(item['price'])*item['quantity']for item in self.cart.values())

    def total(self):
        return self.Anticipos()*self.get_total_price()

    def total2(self):
        return sum((Decimal(item['total_price'])) for item in self.cart.values())

    #def get_total_price_2(self):
        #return self.get_total_price() - self.Anticipos()


    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
    
    
  

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def tax_price(self):
        return (12 / Decimal('100')) * self.total()

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) \
                * self.total()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return  self.total2() - self.get_discount() + self.tax_price() 

  

    

    
