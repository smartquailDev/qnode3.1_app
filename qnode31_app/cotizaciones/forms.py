from django import forms
from .models import ProFit



class ProFitCreateForm(forms.ModelForm):
    class Meta:
        model = ProFit
        fields = ['Maintenance_type', 'activity', 'Maintenance_Zone','Description']
        labels ={ "Maintenance_type":"Tipo de Mantenimiento", "activity": "Rubro de actividad","Description": "Escriba los detalles que usted considere necesaro", "Maintenance_Zone":"Zona de instalación"}
        exclude = ["usuario"]

        help_texts = { 'Description':'Describa su necesidad de mantenimiento' }
        Maintenance_type = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(),label=False),
        activity = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple()),
        Maintenance_Zone = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple()),
        widgets = {
            'Description': forms.Textarea(),              
        }
       
       

    
