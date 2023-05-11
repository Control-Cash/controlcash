from django.shortcuts import render, redirect
from produto.models import Produto
import datetime

# Create your views here.

def home(request):
    produtos = Produto.objects.all()
    return render(request, "home.html", {"produtos": produtos} )

def viewCriarProduto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', None)
        precoVenda = request.POST.get('precoVenda', None)
        descricao = request.POST.get('descricao', None)
        quantidadeEstoque = request.POST.get('quantidadeEstoque', None)
        dataRegistro = datetime.date.today()

        Produto.objects.create(nome=nome, 
                               precoVenda=precoVenda, 
                               descricao=descricao, 
                               quantidadeEstoque=quantidadeEstoque,
                               dataRegistro=dataRegistro)
        
        return redirect('/produto')

    return render(request,'formCriarProduto.html')


def viewVizualizarProduto(request,id):
    if request.method == 'GET':
        produto = Produto.objects.get(id=id)
        return render(request,'vizualizarProduto.html', {"produto": produto})


def viewEditarProduto(request,id):
    produto = Produto.objects.get(id=id)
    return render(request,'formUpdateProduto.html', {"produto": produto})

def viewAtualizarProduto(request,id):
    produto = Produto.objects.get(id=id)

    nome = request.POST.get('nome')
    precoVenda = request.POST.get('precoVenda')
    descricao = request.POST.get('descricao')
    quantidadeEstoque = request.POST.get('quantidadeEstoque')

    produto.nome=nome
    produto.precoVenda=precoVenda
    produto.descricao=descricao
    produto.quantidadeEstoque=quantidadeEstoque

    produto.save()

    return redirect('/produto')
    
def viewDeletarProduto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('/produto')