#from dal import autocomplete
from django.urls import reverse
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Edificios,Cotizacion
from Proyectos.models import Project,mantenimiento
from django.conf import settings
from .tasks import building_created
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.utils.safestring import mark_safe
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions



def building_created(request):
            # launch asynchronous task
            building_created.delay(Edificios.building_name)
            # set the order in the session
            request.session['edificio_id'] = Edificios.building_name
            # redirect for payment
            return render(request,'edificios/edificio/create.html',
                  {'edificio': edificio})


def cotizacion_create(request):
            # launch asynchronous task
            cotizacion_created.delay(cotizacion.project_name)
            # set the order in the session
            request.session['cotizacion_id'] = cotizacion.project_name
            # redirect for payment
            return render(request,'edificios/edificio/cotizacion.html',
                  {'cotizacion': cotizacion})


@staff_member_required
def admin_edificio_detail(request, edificio_id):
    order = get_object_or_404(Edificios, id=edificio_id)
    return render(request,
                  'admin/edificios/edificio/detail.html',
                  {'edificio': edificio})

@staff_member_required
def admin_cotizacion_detail(request, cotizacion_id):
    order = get_object_or_404(Cotizacion, id=cotizacion_id)
    return render(request,
                  'admin/edificios/cotizacion/detail.html',
                  {'cotizacion': cotizacion})

@staff_member_required
def cotizacion_list(request):
    user=None
    categories = mantenimiento.objects.all()
    products =  Cotizacion.objects.filter(paid=True)
    productos =  Cotizacion.objects.filter(Edificio=user)

    return render(request, 
        'cotizaciones/cotizaciones_list.html',  
        {'categories':categories,
        'products':products})

@staff_member_required
def cotizacion_pdf(request, cotizacion_id):
    cotizacion = get_object_or_404(Cotizacion, id=cotizacion_id)
    html = render_to_string('Edificios/Edificio/cotizacion_pdf.html',
                            {'cotizacion': cotizacion})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=cotizacion.project_name_{}.pdf"'.format(cotizacion.project_name)
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response,
        stylesheets=[weasyprint.CSS('static/css/pdf.css'),])
    return render(request, 
        'cotizaciones/cotizaciones_list.html',  
        {'cotizacion':cotizacion})

def cotizacion_pdf(obj):
    return mark_safe('<a href="{}">Cotización</a>'.format(
        reverse('cotizacion:admin_cotizacion_pdf', args=[obj.id])))
cotizacion_pdf.short_description = 'Imprimir'




@staff_member_required
def admin_cotizacion_pdf(request, cotizacion_id):
    cotizacion = get_object_or_404(Cotizacion, id=cotizacion_id)
    html = render_to_string('Edificios/Edificio/cotizacion_pdf.html',
                            {'cotizacion': cotizacion})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=cotizacion.project_name_{}.pdf"'.format(cotizacion.project_name)
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response,
        stylesheets=[weasyprint.CSS('static/css/pdf.css'),])
    return response

@staff_member_required
def admin_edificio_pdf(request, edificio_id):
    edificio = get_object_or_404(Edificios, id=edificio_id)
    html = render_to_string('Edificios/Edificio/edificio_pdf.html',
                            {'edificio': edificio})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=Edificios.building_name{}.pdf"'.format(Edificios.building_name)
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response,
        stylesheets=[weasyprint.CSS('static/css/pdf.css'),])
    return response
