#from dal import autocomplete
from zoneinfo import available_timezones
from django.urls import reverse
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Cotizacion,ProFit,InvoiceItem,Category
from .forms import ProFitCreateForm,CotiCartAddProductForm,CotiCreateForm
#from Proyectos.models import Project,mantenimiento
from django.conf import settings
from .tasks import cotizacion_created
from .coti_cart import Coti_Cart
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.utils.safestring import mark_safe
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions
from django.views.decorators.http import require_POST
from io import BytesIO
from django.core.mail import EmailMessage


#----- Solicitud de cliente de cotizaciones 

def cotizacion_create(request):
    if request.method == 'POST':
        form = ProFitCreateForm(request.POST)
        form.instance.usuario = request.user
        if  form.is_valid():
            coti = form.save(commit=False)
            coti.save()
            # launch asynchronous task
            cotizacion_created.delay(coti.id)
        
            # set the order in the session
            request.session['coti_id'] = coti.id
            # redirect for payment
            return redirect(reverse('payment:done'))
    else:
        form = ProFitCreateForm()
    return render(request,
                  'cotizaciones/profit/create.html',
                  {'form': form})

#------- Lista y detall de cotizaciones-------------

def invoice_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    invoices =  Cotizacion.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        invoices = invoices.filter(category=category)
    return render(request, 
        'cotizaciones/cotizacion/list.html',  
        {'category':category,
        'categories':categories,
        'invoices': invoices})


def invoice_detail(request,id, slug):
    invoice = get_object_or_404(Cotizacion,id=id,slug=slug,available=True)
    coti_cart_invoice_form = CotiCartAddProductForm()
   
    return render(request,'cotizaciones/cotizacion/detail.html',{'invoice':invoice , ' coti_cart_invoice_form': coti_cart_invoice_form} )

#-----------Cartas de Aprobacion---------

@require_POST
def coti_cart_add(request, invoice_id):
    coti_cart = Coti_Cart(request)
    invoice = get_object_or_404(Cotizacion, id=invoice_id)
    form = CotiCartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        coti_cart.add(invoice=invoice,
                 anticipo=cd['anticipo'],
                 quantity=cd['quantity'],
                 #update_anticipo=cd['update_a'],
                 update_quantity=cd['update'])
    return redirect('coti_cart:coti_cart_detail')

def coti_cart_remove(request,invoice_id):
    coti_cart=Coti_Cart(request)
    invoice= get_object_or_404(Cotizacion,id=invoice_id)
    coti_cart.remove(invoice)
    return redirect('coti_cart:coti_cart_detail')

def coti_cart_detail(request):
    coti_cart = Coti_Cart(request)
    return render(request, 'coti_cart/detail.html', {'coti_cart':coti_cart})

#-------Ordenes aprobadas de cotizacion----

def order_coti_create(request):
    coti_cart = Coti_Cart(request)
    if request.method == 'POST':
        form = CotiCreateForm(request.POST)

        if form.is_valid():
            coti = form.save(commit=False)
            coti.save()

            for item in coti_cart:
                InvoiceItem.objects.create(coti=coti,
                                         invoice=item['invoice'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         anticipo= item['anticipo'])
            # clear the cart
            coti_cart.clear()
            # launch asynchronous task
            #order_created.delay(order.id)
            # set the order in the session
            #request.session['order_id'] = order.id
    
            # redirect for payment
            return render(request, 'cotizaciones/cotizacion/created.html', {'coti':coti} )
    else:
        form = CotiCreateForm()
    return render(request,
                  'cotizaciones/cotizacion/create_coti.html',
                  {'coti_cart': coti_cart, 'form': form})

