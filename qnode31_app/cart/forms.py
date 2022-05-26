from django import forms
from django.utils.translation import gettext_lazy as _


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PORCENTAJES = [(i, str(i)) for i in range(50, 101)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,
                                label=_('Cantidad'))
    anticipo = forms.TypedChoiceField(
                                choices=PORCENTAJES,
                                coerce=int,
                                label=_('Anticipo'))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

