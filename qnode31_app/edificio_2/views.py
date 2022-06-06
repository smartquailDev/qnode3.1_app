#from dal import autocomplete
from zoneinfo import available_timezones
from django.urls import reverse
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Cotizacion,Category
#from .forms import ProFitCreateForm,CotiCartAddProductForm,CotiCreateForm
#from Proyectos.models import Project,mantenimiento
from django.conf import settings
#from .tasks import cotizacion_created
#from .coti_cart import Coti_Cart
from edificio_2.cart import Cart
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.utils.safestring import mark_safe
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions
from django.views.decorators.http import require_POST
from io import BytesIO
from django.core.mail import EmailMessage
from .forms import CartAddProductForm

# Create your views here.

#------- Lista y detall de cotizaciones-------------

def invoice_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    invoices =  Cotizacion.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        invoices = invoices.filter(category=category)
    return render(request, 
        'edificio_2/invoice/list.html',  
        {'category':category,
        'categories':categories,
        'invoices': invoices})


def invoice_detail(request,id, slug):
    invoice = get_object_or_404(Cotizacion,id=id,slug=slug, available=True)
    cart_invoice_form = CartAddProductForm()
   
    return render(request,'edificio_2/invoice/detail.html',{'invoice':invoice, 'cart_invoice_form':cart_invoice_form} )

#-----------Cartas de Aprobacion---------

@require_POST
def cart_add(request, invoice_id):
    cart = Cart(request)
    invoice = get_object_or_404(Cotizacion, id=invoice_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(invoice=invoice,
                # anticipo=cd['anticipo'],
                 quantity=cd['quantity'],
                 #update_anticipo=cd['update_a'],
                 update_quantity=cd['update'])
    return redirect('edificio_2:cart_detail')


def cart_remove(request, invoice_id):
    cart = Cart(request)
    invoice = get_object_or_404(Cotizacion, id=invoice_id)
    cart.remove(invoice)
    return redirect('edificio_2:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                              initial={'quantity': item['quantity'],
                              'update': True})
            #item['update_anticipo_form'] = CartAddProductForm(
                             # initial={'anticipo': item['anticipo'],
                             # 'update': True})
   # coupon_apply_form = CouponApplyForm()
    return render(request, 'edificio_2/cart/detail.html', 
    {'cart': cart})