from django.shortcuts import redirect, render

from venda.forms import ClienteForm
from venda.models import Cliente


def criar_cliente_view(request):
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('venda_listar')
    return render(request, 'venda/cliente/criar.html', {'form': form})


def listar_clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'venda/cliente/listar.html', {'clientes': clientes})
