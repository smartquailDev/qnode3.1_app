from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _


app_name = 'cotizacion'

urlpatterns = [
    path('create/', views.cotizacion_create, name='cotizacion_create'),
    path('calendar/',views.CalendarView.as_view(), name='calendar')
]
