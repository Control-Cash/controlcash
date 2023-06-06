from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from venda.forms import EditarItemVendaForm
from venda.models import Item


@require_http_methods(["GET", "POST"])
def editar_quatidade_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    form = EditarItemVendaForm(instance=item)

    if request.method == 'POST':
        form = EditarItemVendaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('venda:venda_detalhar', pk=item.venda.id)
    return render(request, 'venda/item/editar.html', {'form': form, 'item': item})


@require_http_methods(["GET", "POST"])
def remover_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    venda_id = item.venda.id
    if request.method == 'POST':
        item.delete()
        return redirect('venda:venda_detalhar', pk=venda_id)
    return render(request, 'venda/item/remover.html', {'item': item})
