#from dal import autocomplete
from zoneinfo import available_timezones
from django.urls import reverse
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from ProFit.models import Profile
from .models import Coti_Order, Cotizacion,Category,Coti_OrderItem,Project_Order,Project_OrderItem

#from .forms import ProFitCreateForm,CotiCartAddProductForm,CotiCreateForm
#from Proyectos.models import Project,mantenimiento
from django.conf import settings
from .tasks import coti_order_created, project_order_created
#from .coti_cart import Coti_Cart
from edificio_2.cart import Cart
from edificio_2.cart_pay import Cart_Pay
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.utils.safestring import mark_safe
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions
from django.views.decorators.http import require_POST
from io import BytesIO
from django.core.mail import EmailMessage
from .forms import CartAddProductForm,CotiOrderCreateForm,CartAddProjectForm,ProjectOrderCreateForm
from django.db.models import Count


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
                 anticipo=cd['anticipo'])
                 #quantity=cd['quantity'],
                 #update_anticipo=cd['update_a'],
                 #update_quantity=cd['update'])
    return redirect('edificio_2:cart_detail')


def cart_remove(request, invoice_id):
    cart = Cart(request)
    invoice = get_object_or_404(Cotizacion, id=invoice_id)
    cart.remove(invoice)
    return redirect('edificio_2:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
           # item['update_quantity_form'] = CartAddProductForm(
            #                  initial={'quantity': item['quantity'],
             #                 'update': True})
            item['update_anticipo_form'] = CartAddProductForm(
                              initial={'anticipo': item['anticipo'],
                              'update': True})
   # coupon_apply_form = CouponApplyForm()
    return render(request, 'edificio_2/cart/detail.html', 
    {'cart': cart})

#-----------Orden de Cotizacion----------------------

def coti_order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CotiOrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            for item in cart:
                Coti_OrderItem.objects.create(order=order,
                                         invoice=item['invoice'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         anticipo= item['anticipo'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            coti_order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
    
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = CotiOrderCreateForm()
    return render(request,
                  'edificio_2/invoices/invoice/create.html',
                  {'cart': cart, 'form': form})

#--------------Detalles de Ordenes Admin---------------

@staff_member_required
def admin_coti_order_detail(request, order_id):
    order = get_object_or_404(Coti_Order, id=order_id)
    return render(request,
                  'edificio_2/admin/invoices/invoice/detail.html',
                  {'order': order})


@staff_member_required
def admin_coti_order_pdf(request, order_id):
    order = get_object_or_404(Coti_Order, id=order_id)
    html = render_to_string(
        'edificio_2/admin/invoices/invoice/pdf.html',
        {'order':order}
    )
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition']='filename=\ "order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('staticfiles/css/pdf.css')], presentational_hints=True)
    return response


#-------------Lista y historico de cotizaciones-----------------------


def coti_list(request, category_slug=None):
    category = None
    categories = Coti_Order.objects.all()
    invoices =  Coti_Order.objects.filter(aprobe=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        invoices = invoices.filter(category=category)
    return render(request, 
        'edificio_2/coti/list.html',  
        {'category':category,
        'categories':categories,
        'invoices': invoices})

#-------------Lista y historico de proyectos-----------------------

def coti_project_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    invoices =  Coti_Order.objects.filter(aprobe=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        invoices = invoices.filter(category=category)
    return render(request, 
        'edificio_2/proyectos/list.html',  
        {'category':category,
        'categories':categories,
        'invoices': invoices})

def project_detail(request,id, slug):
    invoice = get_object_or_404(Coti_Order,id=id,slug=slug, aprobe=True)
    cart_project_form = CartAddProjectForm() #QUe sea el formulario del plan de trabajo
   
    return render(request,'edificio_2/proyectos/detail.html',{'invoice':invoice, 'cart_project_form':cart_project_form} )

#-----------Cartas de pago---------

@require_POST
def cart_project_add(request, invoice_id):
    cart = Cart_Pay(request)
    invoice = get_object_or_404(Coti_Order, id=invoice_id)
    form = CartAddProjectForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(invoice=invoice,
                 quantity=cd['quantity'],
                 #update_anticipo=cd['update_a'],
                 update_quantity=cd['update'])
    return redirect('edificio_2:cart_project_detail')


def cart_project_remove(request, invoice_id):
    cart = Cart_Pay(request)
    invoice = get_object_or_404(Coti_Order, id=invoice_id)
    cart.remove(invoice)
    return redirect('edificio_2:cart_project_detail')


def cart_project_detail(request):
    cart = Cart_Pay(request)
    for item in cart:
            item['update_quantity_form'] = CartAddProjectForm(
                              initial={'quantity': item['quantity'],
                              'update': True})
   # coupon_apply_form = CouponApplyForm()
    return render(request, 'edificio_2/cart_pay/detail.html', 
    {'cart': cart})

#-----------Orden de Pago de Proyectos----------------------

def project_order_create(request):
    cart = Cart_Pay(request)
    if request.method == 'POST':
        form = ProjectOrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            for item in cart:
                Project_OrderItem.objects.create(order=order,
                                         invoice=item['invoice'],
                                         price1=item['price1'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            project_order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
    
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = ProjectOrderCreateForm()
    return render(request,
                  'edificio_2/invoices/project_invoice/create.html',
                  {'cart': cart, 'form': form})

#--------------Detalles de Ordenes de Proyectos Admin---------------

@staff_member_required
def admin_project_order_detail(request, order_id):
    order = get_object_or_404(Project_Order, id=order_id)
    return render(request,
                  'edificio_2/admin/invoices/project_invoice/detail.html',
                  {'order': order})


@staff_member_required
def admin_project_order_pdf(request, order_id):
    order = get_object_or_404(Project_Order, id=order_id)
    invoices =  Coti_Order.objects.all()
    counts = Project_Order.objects.values("coti").annotate(Count("id"))
    html = render_to_string(
        'edificio_2/admin/invoices/project_invoice/pdf.html',
        {'order':order,'invoices':invoices}
    )
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition']='filename=\ "order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('staticfiles/css/pdf.css')], presentational_hints=True)
    return response