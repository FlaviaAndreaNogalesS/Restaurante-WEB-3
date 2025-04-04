from django import forms
from ordenes.models import Orden, Cliente

class PagoForm(forms.ModelForm):
    #selector
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Cliente que paga"
    )

    class Meta:
        model = Orden
        fields = ['cliente']
