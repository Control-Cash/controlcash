from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from venda.forms import ClienteForm, EnderecoForm
from venda.models import Cliente, Venda


@require_http_methods(["GET", "POST"])
def criar_cliente_view(request):
    form = ClienteForm()
    endereco_cliente_form = EnderecoForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        endereco_cliente_form = EnderecoForm(request.POST)
        if form.is_valid() and endereco_cliente_form.is_valid():
            endereco_salvo = endereco_cliente_form.save()
            cliente_criado = form.save(commit=False)
            cliente_criado.endereco = endereco_salvo
            cliente_criado.save()
            return redirect('venda:cliente_detalhar', cliente_criado.id)
    return render(request, 'venda/cliente/criar.html', {'form': form, 'endereco_form': endereco_cliente_form})


@require_http_methods(["GET"])
def listar_clientes_view(request):
    clientes = Cliente.objects.all().order_by('-id')
    paginator = Paginator(clientes, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'venda/cliente/listar.html', {'page_obj': page_obj})


@require_http_methods(["GET"])
def detalhar_cliente_view(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    vendas = Venda.objects.filter(
        cliente=cliente).order_by('-data', '-hora')[:6]
    return render(request, 'venda/cliente/detalhar.html', {'cliente': cliente, 'vendas': vendas})


@require_http_methods(["GET", "POST"])
def editar_cliente_view(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    form = ClienteForm(instance=cliente)
    endereco_cliente_form = EnderecoForm(instance=cliente.endereco)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        endereco_cliente_form = EnderecoForm(
            request.POST, instance=cliente.endereco)
        if form.is_valid() and endereco_cliente_form.is_valid():
            form.save()
            endereco_cliente_form.save()
            return redirect('venda:cliente_detalhar', pk=pk)
    return render(request, 'venda/cliente/editar.html', {'cliente': cliente, 'form': form, 'endereco_form': endereco_cliente_form})
