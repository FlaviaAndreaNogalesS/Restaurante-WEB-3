from django.shortcuts import render, redirect, get_object_or_404
from ordenes.models import Orden
from ordenes.forms import OrdenForm


def orden_list(request):
    ordenes = Orden.objects.all()
    return render(request, 'ordenes/ordenes/list.html', {'ordenes': ordenes})


def orden_create(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orden_list')
    else:
        form = OrdenForm()
    return render(request, 'ordenes/ordenes/form.html', {'form': form})


def orden_update(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('orden_list')
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'ordenes/ordenes/form.html', {'form': form})


def orden_delete(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('orden_list')
    return render(request, 'ordenes/ordenes/delete_confirm.html', {'orden': orden})
