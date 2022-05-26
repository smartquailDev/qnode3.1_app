from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _


app_name = 'HOMEDETAIL'

urlpatterns = [
    path('admin/HOMEDETAIL/edificios/<int:edificio_id>/', views.admin_edificio_detail, name='admin_edificio_detail'),
    path('admin/HOMEDETAIL/edificios/<int:edificio_id>/pdf/', views.admin_edificio_pdf, name='admin_edificio_pdf'),
    path('admin/HOMEDETAIL/cotizaciones/<int:cotizacion_id>/', views.admin_cotizacion_detail, name='admin_cotizacion_detail'),
    path('admin/HOMEDETAIL/cotizaciones/<int:cotizacion_id>/pdf/', views.admin_cotizacion_pdf, name='admin_cotizacion_pdf'),
    path('HOMEDETAIL/cotizaciones/<int:cotizacion_id>/pdf/', views.cotizacion_pdf, name='cotizacion_pdf'),
    path('cotizaciones_list/', views.cotizacion_list, name='cotizacion_list'),
]
