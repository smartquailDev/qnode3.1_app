from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from edificio_1.models import Cotizacion
from .cart import Cart
from .forms import CartAddProductForm
#from coupons.forms import CouponApplyForm


@require_POST
def cart_add(request, invoice_id):
    cart = Cart(request)
    invoice = get_object_or_404(Cotizacion, id=invoice_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(invoice=invoice,
                 anticipo=cd['anticipo'],
                 quantity=cd['quantity'],
                 #update_anticipo=cd['update_a'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, invoice_id):
    cart = Cart(request)
    invoice = get_object_or_404(Cotizacion, id=invoice_id)
    cart.remove(invoice)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                              initial={'quantity': item['quantity'],
                              'update': True})
            item['update_anticipo_form'] = CartAddProductForm(
                              initial={'anticipo': item['anticipo'],
                              'update': True})
   # coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/detail.html', 
    {'cart': cart})
