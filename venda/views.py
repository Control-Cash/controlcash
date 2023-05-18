from django.shortcuts import get_object_or_404, redirect, render

from venda.forms import ItemVendaForm
from venda.models import Item, Venda


def criar_venda_view(request):
    item_form = ItemVendaForm()

    if request.method == 'POST':
        item_form = ItemVendaForm(request.POST)
        if item_form.is_valid():
            nova_venda = Venda.objects.create()

            novo_item = item_form.save(commit=False)
            novo_item.venda = nova_venda
            novo_item.save()
            return redirect('venda_detalhar', pk=nova_venda.id)
    return render(request, 'venda/criar.html', {'form': item_form})


def listar_vendas_view(request):
    vendas = Venda.objects.all()
    return render(request, 'venda/listar.html', {'vendas': vendas})


def detalhar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    return render(request, 'venda/detalhar.html', {'venda': venda})


def editar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    form = VendaForm(instance=venda)

    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('detalhar_produto', pk=pk)
    return render(request, 'venda/editar.html', {'form': form})


def desativar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    if request.method == 'POST':
        venda.status = False
        venda.save()
        return redirect('venda_listar', pk=pk)
    return render(request, 'venda/desativar.html', {'venda': venda})
