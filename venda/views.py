from django.shortcuts import render, redirect

from venda.forms import VendaForm
from venda.models import Venda


def criar_venda_view(request):
    form = VendaForm()

    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venda_listar')
    return render(request, 'venda/criar_venda.html', {'form': form})

def listar_vendas_view(request):
    vendas = Venda.objects.all()
    return render(request, 'venda/listar_vendas.html', {'vendas': vendas})
