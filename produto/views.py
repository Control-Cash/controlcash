from django.shortcuts import render, redirect
from produto.models import Produto
import datetime
from .forms import CadastrarProduto

# Create your views here.

def home(request):
    produtos = Produto.objects.all()
    return render(request, "home.html", {"produtos": produtos} )

def view_criar_produto(request):
    form = CadastrarProduto()
    if request.method == 'POST':
        form = CadastrarProduto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produto')

    return render(request,'formCriarProduto.html', {"form": form})


def view_vizualizar_produto(request,id):
    if request.method == 'GET':
        produto = Produto.objects.get(id=id)
        return render(request,'vizualizarProduto.html', {"produto": produto})


def view_editar_produto(request,id):
    produto = Produto.objects.get(id=id)
    return render(request,'formUpdateProduto.html', {"produto": produto})

def view_atualizar_produto(request,id):
    produto = Produto.objects.get(id=id)
    form = CadastrarProduto(instance=produto)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/produto')                
        return redirect('/produto')
    
    return render(request,'formUpdateProduto.html', {"produto": produto, "form": form})
        
def view_deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('/produto')