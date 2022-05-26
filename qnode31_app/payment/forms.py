from django import forms
from .models import Check_Payment,Trans_Payment



class CheckForm(forms.ModelForm):
    class Meta:
        model = Check_Payment
        fields = ['Nombre_banco', 'Numero_de_cheque', 'Numero_de_control', 'fecha_de_emision','valor']
        widgets = {
            'Nombre_banco': forms.TextInput(),
            'Numero_de_cheque': forms.TextInput(),
            'Numero_de_control': forms.TextInput(),
            'fecha_de_emision': forms.TextInput(),
            'valor' : forms.TextInput(),
        }
class TransForm(forms.ModelForm):
    class Meta:
        model = Trans_Payment
        fields = ['transferencia']
       

