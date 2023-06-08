from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from produto.models import Produto

from .forms import CadastrarProduto

# Create your views here.

redirect_response = '/produto'


@require_http_methods(["GET"])
def home_produto(request):
    nome_produto = request.GET.get("produto")
    produtos = Produto.objects.all()

    if nome_produto: 
        produtos = Produto.objects.filter(nome__icontains=nome_produto)  
    elif nome_produto == " ":
        produtos = Produto.objects.all()
    return render(request, "home.html", {"produtos": produtos} ) 

@require_http_methods(["GET", "POST"])
def view_criar_produto(request):
    form = CadastrarProduto()
    if request.method == 'POST':
        form = CadastrarProduto(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_response)

    return render(request, 'formCriarProduto.html', {"form": form})


@require_http_methods(["GET"])
def view_vizualizar_produto(request, id):
    if request.method == 'GET':
        produto = Produto.objects.get(id=id)
        return render(request, 'vizualizarProduto.html', {"produto": produto})


@require_http_methods(["GET"])
def view_editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'formUpdateProduto.html', {"produto": produto})


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

    return render(request, 'formUpdateProduto.html', {"produto": produto, "form": form})


@require_http_methods(["GET"])
def view_deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(redirect_response)
