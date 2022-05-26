from __future__ import unicode_literals
import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Edificios,Proyecto,Analitycs,Analitycs2,PlandeTrabajo,Cotizacion,InvoiceItem,Diagnostico,Facturacion
from django.urls import reverse
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin
from django.utils.translation import gettext_lazy as _
from django.db.models import F,Value,Count,Avg, Sum, Min, Max, DateTimeField
from django.db.models.functions import TruncDay,Trunc


def edificio_detail(obj):
    return mark_safe('<a href="{}">Perfil</a>'.format(
        reverse('edificio:admin_edificio_detail', args=[obj.id])))


def edificio_pdf(obj):
    return mark_safe('<a href="{}">Ficha Técnica</a>'.format(
        reverse('edificio:admin_edificio_pdf', args=[obj.id])))
edificio_pdf.short_description = 'Imprimir'


def cotizacion_pdf(obj):
    return mark_safe('<a href="{}">Cotización</a>'.format(
        reverse('cotizacion:admin_cotizacion_pdf', args=[obj.id])))
cotizacion_pdf.short_description = 'Imprimir'





@admin.register(Edificios)
class EdificiosAdmin(TranslatableAdmin):
    list_display = ['building_name','created','updated' ,
                    'administration_manager',edificio_pdf]


class AnalitycsItemInline(admin.TabularInline):
    readonly_fields = ["total2",]
    model = Analitycs

class Analitycs2ItemInline(admin.TabularInline):
    readonly_fields = ["total1",]
    model = Analitycs2
class PlandeTrabajoItemInline(admin.TabularInline):
    readonly_fields = ["total",]
    model = PlandeTrabajo
  

def get_next_in_date_hierarchy(request, date_hierarchy):
    
    if date_hierarchy + '__day' in request.GET:
        return 'hour'
    if date_hierarchy + '__month' in request.GET:
        return 'day'
    if date_hierarchy + '__year' in request.GET:
        return 'week'
    return 'month'

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    raw_id_fields = ['project']


@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = [ 'Edificio','project_name', 'paid','paid2','report_code', 'email','created', 'updated',cotizacion_pdf]
    list_filter = ['project_name', 'created', 'updated']
    inlines = [InvoiceItemInline]
    readonly_fields = ["code",]



@admin.register(Diagnostico)
class DiagnosticoAdmin(TranslatableAdmin):
    list_display = ['Codigo','project_name2','created','date_meet','dayswork',]
    readonly_fields = ['code',]





@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['project_name','Advance','Anticipo','Avance_de_Obra','Fecha']
    readonly_fields = ["value3","value4"]

@admin.register(Facturacion)
class FacturacionAdmin(TranslatableAdmin):
    list_display = ['Egreso_num','Edificio','project_name','created','numero_cheque']
    







