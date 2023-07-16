from django.shortcuts import render,redirect
from .models import *
from venda.models import Endereco
from venda.forms import EnderecoForm
from .forms import CadastrarFornecedor

redirect_response = '/fornecedor'

def listar_fornecedores(request):
    nome_do_fornecedor = request.GET.get('fornecedor')
    fornecedores = Fornecedor.objects.all()

    if nome_do_fornecedor:
        fornecedores = Fornecedor.objects.filter(nome__icontains=nome_do_fornecedor)
    elif nome_do_fornecedor == " ":
        fornecedores = Fornecedor.objects.all()
    return render(request, 'homeFornecedores.html', {'fornecedores': fornecedores})

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
