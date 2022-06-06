from __future__ import unicode_literals
import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Cotizacion,Category
from django.urls import reverse
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin
from django.utils.translation import gettext_lazy as _
from django.db.models import F,Value,Count,Avg, Sum, Min, Max, DateTimeField
from django.db.models.functions import TruncDay,Trunc

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