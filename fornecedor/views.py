from django.shortcuts import render,redirect
from .models import *
from venda.models import Endereco
from venda.forms import EnderecoForm
from .forms import CadastrarFornecedor
from django.views.decorators.http import require_http_methods

redirect_response = '/fornecedor'

@require_http_methods(["GET"])
def listar_fornecedores(request):
    nome_do_fornecedor = request.GET.get('fornecedor')
    fornecedores = Fornecedor.objects.all()

    if nome_do_fornecedor:
        fornecedores = Fornecedor.objects.filter(nome__icontains=nome_do_fornecedor)
    elif nome_do_fornecedor == " ":
        fornecedores = Fornecedor.objects.all()
    return render(request, 'homeFornecedores.html', {'fornecedores': fornecedores})

@require_http_methods(["GET", "POST"])
def cadastrar_fornecedor(request):
    form = CadastrarFornecedor
    form_endereco = EnderecoForm
    if request.method == 'POST':
        form = CadastrarFornecedor(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form.is_valid() and form_endereco.is_valid():
            endereco_salvo = form_endereco.save()
            fornecedor_criado = form.save(commit=False)
            fornecedor_criado.endereco = endereco_salvo
            fornecedor_criado.save() 
            return redirect(redirect_response)

    return render(request, 'formCriarForcedor.html', {"form": form, 'endereco_form': form_endereco})

@require_http_methods(["GET", "POST"])
def atualizar_fornecedor(request,id):
    fornecedor = Fornecedor.objects.get(id=id)
    endereco = fornecedor.endereco
    form = CadastrarFornecedor(instance=fornecedor)
    form_endereco = EnderecoForm(instance=endereco)
    if request.method == 'POST':
        form = CadastrarFornecedor(request.POST, instance=fornecedor)
        form_endereco = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid() and form_endereco.is_valid():
            endereco_salvo = form_endereco.save()
            fornecedor_atualizado = form.save(commit=False)
            fornecedor_atualizado.endereco = endereco_salvo
            fornecedor_atualizado.save()
            return redirect(redirect_response)
    return render(request,'formAtualizaFornecedor.html', {'fornecedor': fornecedor, 'form': form, 'endereco_form': form_endereco})

@require_http_methods(["GET"])
def vizualizar_fornecedor(request, id):
    if request.method == 'GET':
        fornecedor = Fornecedor.objects.get(id=id)
        return render(request, 'vizualizarFornecedor.html', {'fornecedor': fornecedor})

@require_http_methods(["GET", "POST"])
def deletar_fornecedor(request,id):
    fornecedor = Fornecedor.objects.get(id=id)
    fornecedor.delete()
    return redirect(redirect_response)