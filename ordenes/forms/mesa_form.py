from django import forms
from ordenes.models import Mesa


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
        }
