from django import forms
from ordenes.models import Orden, Plato, Mesero, Mesa, Cliente
from django.core.exceptions import ValidationError

class OrdenForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        mesa = cleaned_data.get('mesa')
        estado = cleaned_data.get('estado')

        if estado == 'abierto' and mesa:
            #validación pa no repetir mesas
            orden_abierta = Orden.objects.filter(mesa=mesa, estado='abierto')

            # editar una orden, se excluye a sí misma
            if self.instance.pk:
                orden_abierta = orden_abierta.exclude(pk=self.instance.pk)

            if orden_abierta.exists():
                raise ValidationError(f"Ya hay una orden abierta para la Mesa {mesa.numero}.")

    #selectores y campos
    platos = forms.ModelMultipleChoiceField(
        queryset=Plato.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        required=True,
        label="Selecciona los platos"
    )
    mesero = forms.ModelChoiceField(
        queryset=Mesero.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Mesero"
    )
    mesa = forms.ModelChoiceField(
        queryset=Mesa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Mesa"
    )
    fecha_hora = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'}
        ),
        label="Fecha y Hora"
    )

    class Meta:
        model = Orden
        fields = ['platos', 'mesero', 'mesa', 'estado', 'fecha_hora']
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
