from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from produto.models import Produto
from venda.models import Venda

from .forms import CadastrarProduto

# Create your views here.

redirect_response = '/produto'


@require_http_methods(["GET"])
def home_produto(request):
    nome_produto = request.GET.get("produto")
    produtos = None

    if nome_produto:
        nome_produto = nome_produto.strip()
        produtos = Produto.objects.filter(
            nome__icontains=nome_produto).order_by('-id')
    else:
        produtos = Produto.objects.all().order_by('-id')

    paginator = Paginator(produtos, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "produto/home.html", {"page_obj": page_obj, "pesquisa": nome_produto})


@require_http_methods(["GET", "POST"])
def view_criar_produto(request):
    form = CadastrarProduto()
    if request.method == 'POST':
        form = CadastrarProduto(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_response)

    return render(request, 'produto/formCriarProduto.html', {"form": form})


@require_http_methods(["GET"])
def view_vizualizar_produto(request, id):
    if request.method == 'GET':
        produto = Produto.objects.get(id=id)
        vendas = Venda.objects.filter(
            item__produto=produto).order_by('-id')[:6]
        return render(request, 'produto/vizualizarProduto.html', {"produto": produto, "vendas": vendas})


@require_http_methods(["GET"])
def view_editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'produto/formUpdateProduto.html', {"produto": produto})


@require_http_methods(["GET", "POST"])
def view_atualizar_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = CadastrarProduto(instance=produto)
    if request.method == 'POST':
        form = CadastrarProduto(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect(redirect_response)
        return redirect(redirect_response)

    return render(request, 'produto/formUpdateProduto.html', {"produto": produto, "form": form})


@require_http_methods(["GET"])
def view_deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(redirect_response)
