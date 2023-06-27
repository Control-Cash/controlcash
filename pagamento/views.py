from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods

from pagamento.models import FormaPagamento, Pagamento
from pagamento.forms import FormaPagamentoForm, PagamentoForm

redirect_response = '/pagamento'

SUCCESS_REDIRECT_URL = 'pagamento:home_pagamento'

@require_http_methods(["GET"])
def home_pagamento_view(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'lista_pagamento.html', {"pagamentos": pagamentos})

@require_http_methods(["GET", "POST"])
def criar_pagamento_view(request):

    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            # Salvar os dados do formulário
            form.save()
            return redirect('/pagamento')
    else:
        form = PagamentoForm()
    
    return render(request, 'criarPagamento.html', {'form': form})

@require_http_methods(["GET", "POST"])
def editar_pagamento_view(request, pk):
    pagamento_obj = get_object_or_404(Pagamento, id=pk)
    form = PagamentoForm(instance=pagamento_obj)

    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento_obj)
        if form.is_valid():
            form.save()
            return redirect(SUCCESS_REDIRECT_URL)
    return render(request, 'editar_pagamento.html', {'form': form})

 