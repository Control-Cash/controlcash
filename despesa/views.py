from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from despesa.forms import DespesaForm
from despesa.models import Despesa


SUCCESS_REDIRECT_URL = 'despesa:despesa_listar'


@require_GET
def listar_despesas_view(request):
    despesas = Despesa.objects.all()
    return render(request, 'despesa/listar.html', {"despesas": despesas})


@require_http_methods(["GET", "POST"])
def criar_despesa_view(request):
    form = DespesaForm()

    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(SUCCESS_REDIRECT_URL)
    return render(request, 'despesa/criar.html', {'form': form})


@require_http_methods(["GET", "POST"])
def editar_despesa_view(request, pk):
    despesa = get_object_or_404(Despesa, id=pk)
    form = DespesaForm(instance=despesa)

    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect(SUCCESS_REDIRECT_URL)
    return render(request, 'despesa/editar.html', {'despesa': despesa, 'form': form})


@require_http_methods(["GET", "POST"])
def remover_despesa_view(request, pk):
    despesa = get_object_or_404(Despesa, id=pk)
    if request.method == 'POST':
        despesa.delete()
        return redirect(SUCCESS_REDIRECT_URL)
    return render(request, 'despesa/remover.html', {'despesa': despesa})
