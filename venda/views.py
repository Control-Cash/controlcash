from django.shortcuts import get_object_or_404, redirect, render

from venda.forms import EditarItemVendaForm, ItemVendaForm
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
    item_form = ItemVendaForm()

    if request.method == 'POST':
        item_form = ItemVendaForm(request.POST)
        if (item_form.is_valid()):
            novo_item = item_form.save(commit=False)

            # verifica se o item já existe na venda
            item_ja_cadastrado = Item.objects.filter(
                venda=venda.id, produto=novo_item.produto).exists()

            if (item_ja_cadastrado):
                item_existente = Item.objects.get(
                    venda=venda.id, produto=novo_item.produto)
                item_existente.quantidade = item_existente.quantidade + novo_item.quantidade
                item_existente.save()

            else:
                novo_item.venda = venda
                novo_item.save()
            return redirect('venda_detalhar', pk=pk)

    context = {
        'venda': venda,
        'form': item_form
    }
    return render(request, 'venda/detalhar.html', context)


def desativar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    if request.method == 'POST':
        venda.status = Venda.STATUS_CHOICES[1][0]
        venda.save()
        return redirect('venda_listar')
    return render(request, 'venda/desativar.html', {'venda': venda})


def finalizar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    if request.method == 'POST':
        venda.status = Venda.STATUS_CHOICES[2][0]
        venda.save()
        return redirect('venda_detalhar', pk=pk)
    return render(request, 'venda/finalizar.html', {'venda': venda})


def reativar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    if request.method == 'POST':
        venda.status = Venda.STATUS_CHOICES[0][0]
        venda.save()
        return redirect('venda_detalhar', pk=pk)
    return render(request, 'venda/reativar.html', {'venda': venda})


def editar_quatidade_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    form = EditarItemVendaForm(instance=item)

    if request.method == 'POST':
        form = EditarItemVendaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('venda_detalhar', pk=item.venda.id)
    return render(request, 'venda/item/editar.html', {'form': form, 'item': item})


def remover_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    venda_id = item.venda.id
    if request.method == 'POST':
        item.delete()
        return redirect('venda_detalhar', pk=venda_id)
    return render(request, 'venda/item/remover.html', {'item': item})
