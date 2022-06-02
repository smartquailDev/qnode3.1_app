from __future__ import unicode_literals
import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import ProFit,Proyecto,Cotizacion,InvoiceItem,Visit,Diagnostico,Category, order_cotizacion
from django.urls import reverse
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin
from django.utils.translation import gettext_lazy as _
from django.db.models import F,Value,Count,Avg, Sum, Min, Max, DateTimeField
from django.db.models.functions import TruncDay,Trunc


@admin.register(Diagnostico)
class DiagnosticoAdmin(TranslatableAdmin):
    list_display = ['Codigo','project_name2','quantity','price','Unit','sub_total','total','dayswork',]
    readonly_fields = ['code',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['maintenace_type', 'slug']
    prepopulated_fields = {'slug':('maintenace_type',)}

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = [ 'Edificio','project_name','price','available']
    list_editable = ['price','available']
    list_filter = ['project_name', 'created', 'updated']
    prepopulated_fields = {'slug':('project_name',)}
    readonly_fields = ["code",]

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    raw_id_fields = ['coti']

@admin.register(order_cotizacion)
class order_cotizacionAdmin(admin.ModelAdmin):
    list_display = [ 'code','email','aprobe','diss']
    list_filter = ['aprobe',]
    inlines = [InvoiceItemInline]
