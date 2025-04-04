from django.shortcuts import render, redirect, get_object_or_404
from ordenes.models import Cliente
from ordenes.forms import ClienteForm


def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'ordenes/clientes/list.html', {'clientes': clientes})


def clientes_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST) #form con datos enviados
        if form.is_valid():
            form.save() #lo guarda
            return redirect('clientes_list') #redirije
    else:
        form = ClienteForm()
    return render(request, 'ordenes/clientes/form.html', {'form': form})


def clientes_update(request, id):
    cliente = get_object_or_404(Cliente, id=id) #busca por id
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'ordenes/clientes/form.html', {'form': form})


def clientes_delete(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes_list')
    return render(request, 'ordenes/clientes/delete_confirm.html', {'cliente': cliente})
