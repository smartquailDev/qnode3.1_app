from django.urls import path,re_path,include
from . import views
from django.utils.translation import gettext_lazy as _


app_name = 'edificio_1'

urlpatterns = [
   # path('create/', views.cotizacion_create, name='cotizacion_create'),
   # path('coti_create/', views.coti_create, name='coti_create'),
    #path('create/', views.order_create, name='order_create'),
    #path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
   # path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
   # path('calendar/',views.CalendarView.as_view(), name='calendar'),
   # path('edificio_1/cotizaciones/<int:cotizacion_id>/pdf/', views.cotizacion_pdf, name='cotizacion_pdf'),
   # path('admin/edificio_1/cotizaciones/<int:cotizacion_id>/pdf/', views.admin_cotizacion_pdf, name='admin_cotizacion_pdf')
    path('cotizaciones/', views.invoice_list, name='invoice_list'),
    path('cotizaciones/<slug:category_slug>/', views.invoice_list, name='invoice_list_by_category'),
    path('cotizaciones/<int:id>/<slug:slug>/', views.invoice_detail,name='invoice_detail'),

   # path('cotizaciones/cotizacion/<int:coti_id>/pdf/', views.admin_invoice_pdf, name='admin_invoice_pdf'),
   # path('cotizaciones/cotizacion/<int:coti_id>/pdf/', views.invoice_pdf, name='invoice_pdf'),
    path('coti_cart/', views.coti_cart_detail, name='coti_cart_detail'),
    path('coti_cart/add/<int:invoice_id>/', views.coti_cart_add, name='coti_cart_add'),
    path('coti_cart/remove/<int:invoice_id>/', views.coti_cart_remove, name='coti_cart_remove'),
    path('orders/create/',views.order_coti_create, name='order_coti_create')
   # path('process/', views.cotizacion_process, name='process'),
   # path('done/', views.cotizacion_done, name='done'),
   # path('canceled/', views.cotizacion_canceled, name='canceled'),
   # path('qr_code/', include('qr_code.urls', namespace="qr_code")),
]
