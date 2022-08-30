from django import forms
from .models import Cotizacion,Coti_Order,Project_Order
import datetime
from django.contrib.admin import widgets 
from core.widgets import BootstrapDateTimePickerInput


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PORCENTAJES = [(i, str(i)) for i in range(50, 101)]


class CartAddProductForm(forms.Form):
    #quantity = forms.TypedChoiceField(
                               # choices=PRODUCT_QUANTITY_CHOICES,
                               # coerce=int,
                               # label='Cantidad',widget=forms.HiddenInput)
    anticipo = forms.TypedChoiceField(
                                choices=PORCENTAJES,
                                coerce=int,
                                label='Elija el porcentaje de anticipo que desea pagar')
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class CartAddProjectForm(forms.Form):

    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,
                                label='Cantidad',
                               )

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)



class ProjectOrderCreateForm(forms.ModelForm):
    
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

    class Meta:
        model=Project_Order
        fields = [ 'email', 'RUC2','project_code']

class CotiOrderCreateForm(forms.ModelForm):
    class Meta:
        model = Coti_Order
        fields = [ 'email', 'RUC2', 'coti_code','aprobe']