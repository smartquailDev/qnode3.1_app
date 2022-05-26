from django.contrib import admin
from .models import Check_Payment,Trans_Payment

@admin.register(Check_Payment)
class Check_PaymentAdmin(admin.ModelAdmin):
    list_display = ['Numero_de_cheque', 'fecha_de_emision','Nombre_banco','valor']

@admin.register(Trans_Payment)
class Trans_PaymentAdmin(admin.ModelAdmin):
    list_display = ['transferencia']