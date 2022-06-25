from django.urls import path,re_path,include
from . import views
from django.utils.translation import gettext_lazy as _


app_name = 'edificio_2'

urlpatterns = [
    path('cotizaciones/', views.invoice_list, name='invoice_list'),
    path('cotizaciones/<slug:category_slug>/', views.invoice_list, name='invoice_list_by_category'),
    path('cotizaciones/<int:id>/<slug:slug>/', views.invoice_detail,name='invoice_detail'),
    
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:invoice_id>/',views.cart_add, name='cart_add'),
    path('remove/<int:invoice_id>/', views.cart_remove, name='cart_remove'),

    path('coti_create/', views.coti_order_create, name='coti_order_create'),
    path('admin/coti_order/<int:order_id>/', views.admin_coti_order_detail, name='admin_coti_order_detail'),
    path('admin/coti_order/<int:order_id>/pdf/', views.admin_coti_order_pdf, name='admin_coti_order_pdf'),

    path('coti_list/', views.coti_list, name='coti_list'),

    path('proyectos/', views.coti_project_list, name='coti_project_list'),
    path('proyectos/<slug:category_slug>/', views.coti_project_list, name='project_list_by_category'),
    #path('cotizaciones/<int:id>/<slug:slug>/', views.invoice_detail,name='invoice_detail'),
]