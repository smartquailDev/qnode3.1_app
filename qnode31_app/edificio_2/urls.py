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
    path('proyectos/<int:id>/<slug:slug>/', views.project_detail, name='project_detail'),

    path('cart_pay/', views.cart_project_detail, name='cart_project_detail'),
    path('cart_pay/add/<int:invoice_id>/',views.cart_project_add, name='cart_project_add'),
    path('cart_pay/remove/<int:invoice_id>/', views.cart_project_remove, name='cart_project_remove'),

    path('project_create/', views.project_order_create, name='project_order_create'),
    path('admin/project_order/<int:order_id>/', views.admin_project_order_detail, name='admin_project_order_detail'),
    path('admin/project_order/<int:order_id>/pdf/', views.admin_project_order_pdf, name='admin_project_order_pdf'),

    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]