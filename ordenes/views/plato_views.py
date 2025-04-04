from django.shortcuts import render, redirect, get_object_or_404
from ordenes.models import Plato
from ordenes.forms import PlatoForm


def plato_list(request):
    platos = Plato.objects.all()
    return render(request, 'ordenes/platos/list.html', {'platos': platos})


def plato_create(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plato_list')
    else:
        form = PlatoForm()
    return render(request, 'ordenes/platos/form.html', {'form': form})


def plato_update(request, id):
    plato = get_object_or_404(Plato, id=id)
    if request.method == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('plato_list')
    else:
        form = PlatoForm(instance=plato)
    return render(request, 'ordenes/platos/form.html', {'form': form})


def plato_delete(request, id):
    plato = get_object_or_404(Plato, id=id)
    if request.method == 'POST':
        plato.delete()
        return redirect('plato_list')
    return render(request, 'ordenes/platos/delete_confirm.html', {'plato': plato})
