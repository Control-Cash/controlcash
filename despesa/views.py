from django.shortcuts import redirect, render
from despesa.forms import DespesaForm

from despesa.models import Despesa


def listar_despesas_view(request):
    despesas = Despesa.objects.all()
    return render(request, 'despesa/listar.html', {"despesas": despesas})


def criar_despesa_view(request):
    form = DespesaForm()

    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('despesa:despesa_listar')
    return render(request, 'despesa/criar.html', {'form': form})
