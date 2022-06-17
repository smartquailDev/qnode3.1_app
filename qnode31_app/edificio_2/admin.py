from __future__ import unicode_literals
import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Cotizacion,Category,Coti_Order,Coti_OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin
from django.utils.translation import gettext_lazy as _
from django.db.models import F,Value,Count,Avg, Sum, Min, Max, DateTimeField
from django.db.models.functions import TruncDay,Trunc

def coti_order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('edificio_2:admin_coti_order_detail', args=[obj.id])))

def coti_order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('edificio_2:admin_coti_order_pdf', args=[obj.id])))
coti_order_pdf.short_description = 'Invoice'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = [ 'name','price','available']
    list_editable = ['price','available']
    list_filter = ['name', 'created', 'updated']
    prepopulated_fields = {'slug':('name',)}
    readonly_fields = ["code",]

class Coti_OrderItemInline(admin.TabularInline):
    model = Coti_OrderItem
    raw_id_fields = ['invoice']

@admin.register(Coti_Order)
class Coti_OrderAdmin(admin.ModelAdmin):
    list_display = ['email',
                   'RUC2', 'aprobe',
                    'created', 'updated',coti_order_detail,coti_order_pdf]
    list_filter = ['aprobe', 'created', 'updated']
    inlines = [Coti_OrderItemInline]

