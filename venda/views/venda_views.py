
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from venda.forms import CriarVendaForm, ItemVendaForm
from venda.models import Item, Venda

NOME_ROTA_DETALHAR_VENDA = 'venda:venda_detalhar'


@require_http_methods(["GET", "POST"])
def criar_venda_view(request):
    form = CriarVendaForm()

    if request.method == 'POST':
        form = CriarVendaForm(request.POST)
        if form.is_valid():
            nova_venda = Venda.objects.create(
                cliente=form.cleaned_data['cliente'])

            novo_item = form.save(commit=False)
            novo_item.venda = nova_venda
            novo_item.save()
            return redirect(NOME_ROTA_DETALHAR_VENDA, pk=nova_venda.id)
    return render(request, 'venda/venda/criar.html', {'form': form})


@require_http_methods(["GET"])
def listar_vendas_view(request):
    vendas = Venda.objects.all().order_by("status", "-data", "-hora")
    return render(request, 'venda/venda/listar.html', {'vendas': vendas})


@require_http_methods(["GET", "POST"])
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
            return redirect(NOME_ROTA_DETALHAR_VENDA, pk=pk)

    context = {
        'venda': venda,
        'form': item_form
    }
    return render(request, 'venda/venda/detalhar.html', context)


@require_http_methods(["GET", "POST"])
def desativar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    if request.method == 'POST':
        venda.status = Venda.STATUS_CHOICES[1][0]
        venda.save()
        return redirect(NOME_ROTA_DETALHAR_VENDA, pk=pk)
    return render(request, 'venda/venda/desativar.html', {'venda': venda})


@require_http_methods(["GET", "POST"])
def finalizar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    if request.method == 'POST':
        venda.status = Venda.STATUS_CHOICES[2][0]
        venda.save()
        return redirect(NOME_ROTA_DETALHAR_VENDA, pk=pk)
    return render(request, 'venda/venda/finalizar.html', {'venda': venda})


@require_http_methods(["GET", "POST"])
def reativar_venda_view(request, pk):
    venda = get_object_or_404(Venda, id=pk)
    if request.method == 'POST':
        venda.status = Venda.STATUS_CHOICES[0][0]
        venda.save()
        return redirect(NOME_ROTA_DETALHAR_VENDA, pk=pk)
    return render(request, 'venda/venda/reativar.html', {'venda': venda})
