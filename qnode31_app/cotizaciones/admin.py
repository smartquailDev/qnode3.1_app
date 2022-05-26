from django.contrib import admin
from .models import ProFit, Visit

@admin.register(ProFit)
class ProFitAdmin(admin.ModelAdmin):
    list_display = ['usuario','Maintenance_type', 'activity', 'Maintenance_Zone','created']

admin.site.register(Visit)
