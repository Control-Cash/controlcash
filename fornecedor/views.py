from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods

from venda.forms import EnderecoForm

from .forms import CadastrarFornecedor
from .models import *

redirect_response = 'fornecedor_listar'


@require_http_methods(["GET"])
def listar_fornecedores(request):
    nome_do_fornecedor = request.GET.get('fornecedor')
    fornecedores = None

    if nome_do_fornecedor:
        nome_do_fornecedor = nome_do_fornecedor.strip()
        fornecedores = Fornecedor.objects.filter(
            nome__icontains=nome_do_fornecedor
        ).order_by('-id')
    else:
        fornecedores = Fornecedor.objects.all().order_by('-id')

    paginator = Paginator(fornecedores, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'homeFornecedores.html', {'page_obj': page_obj, 'pesquisa': nome_do_fornecedor})


@require_http_methods(["GET", "POST"])
def cadastrar_fornecedor(request):
    form = CadastrarFornecedor()
    form_endereco = EnderecoForm()
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
def atualizar_fornecedor(request, id):
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
    return render(request, 'formAtualizaFornecedor.html', {'fornecedor': fornecedor, 'form': form, 'endereco_form': form_endereco})


@require_http_methods(["GET"])
def vizualizar_fornecedor(request, id):
    if request.method == 'GET':
        fornecedor = get_object_or_404(Fornecedor, id=id)
        return render(request, 'vizualizarFornecedor.html', {'fornecedor': fornecedor})


@require_http_methods(["GET", "POST"])
def deletar_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    fornecedor.delete()
    return redirect(redirect_response)
