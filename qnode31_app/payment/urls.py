from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('payment_check/', views.payment_check_process, name='payment_check_process'),
    path('payment_trans/', views.payment_trans_process, name='payment_trans_process'),
]
