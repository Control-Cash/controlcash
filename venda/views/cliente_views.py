from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from venda.forms import ClienteForm
from venda.models import Cliente


@require_http_methods(["GET", "POST"])
def criar_cliente_view(request):
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            cliente_criado = form.save()
            return redirect('venda:cliente_detalhar', cliente_criado.id)
    return render(request, 'venda/cliente/criar.html', {'form': form})


@require_http_methods(["GET"])
def listar_clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'venda/cliente/listar.html', {'clientes': clientes})


@require_http_methods(["GET"])
def detalhar_cliente_view(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    return render(request, 'venda/cliente/detalhar.html', {'cliente': cliente})


@require_http_methods(["GET", "POST"])
def editar_cliente_view(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    form = ClienteForm(instance=cliente)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('venda:cliente_detalhar', pk=pk)
    return render(request, 'venda/cliente/editar.html', {'form': form})
