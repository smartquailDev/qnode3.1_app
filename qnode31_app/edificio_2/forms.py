from django import forms
from .models import Cotizacion,Coti_Order
import datetime
from django.contrib.admin import widgets 


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PORCENTAJES = [(i, str(i)) for i in range(50, 101)]


class CartAddProductForm(forms.Form):
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


class CotiOrderCreateForm(forms.ModelForm):
    class Meta:
        model = Coti_Order
        fields = [ 'email', 'RUC2', 'coti_code','aprobe']
