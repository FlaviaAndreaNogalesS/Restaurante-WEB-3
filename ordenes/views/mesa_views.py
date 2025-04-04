from django.shortcuts import render, redirect, get_object_or_404
from ordenes.models import Mesa
from ordenes.forms import MesaForm


def mesa_list(request):
    mesas = Mesa.objects.all()
    return render(request, 'ordenes/mesas/list.html', {'mesas': mesas})


def mesa_create(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mesa_list')
    else:
        form = MesaForm()
    return render(request, 'ordenes/mesas/form.html', {'form': form})


def mesa_update(request, id):
    mesa = get_object_or_404(Mesa, id=id)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('mesa_list')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'ordenes/mesas/form.html', {'form': form})


def mesa_delete(request, id):
    mesa = get_object_or_404(Mesa, id=id)
    if request.method == 'POST':
        mesa.delete()
        return redirect('mesa_list')
    return render(request, 'ordenes/mesas/delete_confirm.html', {'mesa': mesa})
