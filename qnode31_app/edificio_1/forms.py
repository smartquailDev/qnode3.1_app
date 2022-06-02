from django import forms
from .models import Cotizacion, ProFit, order_cotizacion
import datetime
from django.contrib.admin import widgets 




class ProFitCreateForm(forms.ModelForm):
    class Meta:
        model = ProFit
        fields = ['Maintenance_type', 'activity', 'Maintenance_Zone','Description','visit']
        labels ={ "Maintenance_type":"Tipo de Mantenimiento", "activity": "Rubro de actividad","Description": "Escriba los detalles que usted considere necesaro", "Maintenance_Zone":"Zona de instalación","visit":"Indique una fecha para una visita técnica. (Ej. mes/día/año hs:min:sec)" ,}
        exclude = ["usuario"]

        help_texts = { 'Description':'Describa su necesidad de mantenimiento' }
        Maintenance_type = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(),label=False),
        activity = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple()),
        Maintenance_Zone = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple()),
        visit = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime),
        widgets = {
            'Description': forms.Textarea(),  
                    
        }

class CotiCreateForm(forms.ModelForm):
    class Meta:
        model = order_cotizacion
        fields = ['code','email','aprobe','diss']
       
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PORCENTAJES = [(i, str(i)) for i in range(50, 101)]


class CotiCartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,
                                label='Cantidad')
    anticipo = forms.TypedChoiceField(
                                choices=PORCENTAJES,
                                coerce=int,
                                label='Anticipo')
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

       

    
