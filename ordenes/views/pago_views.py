from django.shortcuts import render, redirect, get_object_or_404
from ordenes.models import Orden
from ordenes.forms.pago_form import PagoForm

def orden_pagar(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        form = PagoForm(request.POST, instance=orden) #carga datos
        if form.is_valid():
            orden = form.save(commit=False) #guarda cliente
            orden.estado = 'cerrado' #cambia estado
            orden.save()
            return redirect('orden_list')
    else:
        form = PagoForm(instance=orden)
    return render(request, 'ordenes/ordenes/pago.html', {'form': form, 'orden': orden})
