from django.shortcuts import render, redirect, get_object_or_404
from ordenes.models import Mesero
from ordenes.forms import MeseroForm


def mesero_list(request):
    meseros = Mesero.objects.all()
    return render(request, 'ordenes/meseros/list.html', {'meseros': meseros})


def mesero_create(request):
    if request.method == 'POST':
        form = MeseroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mesero_list')
    else:
        form = MeseroForm()
    return render(request, 'ordenes/meseros/form.html', {'form': form})


def mesero_update(request, id):
    mesero = get_object_or_404(Mesero, id=id)
    if request.method == 'POST':
        form = MeseroForm(request.POST, instance=mesero)
        if form.is_valid():
            form.save()
            return redirect('mesero_list')
    else:
        form = MeseroForm(instance=mesero)
    return render(request, 'ordenes/meseros/form.html', {'form': form})


def mesero_delete(request, id):
    mesero = get_object_or_404(Mesero, id=id)
    if request.method == 'POST':
        mesero.delete()
        return redirect('mesero_list')
    return render(request, 'ordenes/meseros/delete_confirm.html', {'mesero': mesero})
