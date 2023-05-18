from django.shortcuts import get_object_or_404, redirect, render

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

def detalhar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    return render(request, 'venda/detalhar_venda.html', {'venda': venda})