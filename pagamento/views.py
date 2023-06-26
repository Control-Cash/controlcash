from django.shortcuts import get_object_or_404, render, redirect

from pagamento.models import FormaPagamento, Pagamento
from pagamento.forms import FormaPagamentoForm, PagamentoForm

redirect_response = '/pagamento'


def home_pagamento_view(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'lista_pagamento.html', {"pagamentos": pagamentos})

""" def home_pagamento(request):
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            # Salvar os dados do formulário
            form.save()
            return redirect('/pagamento')
    else:
        form = PagamentoForm()
    
    return render(request, 'lista_pagamento.html', {'form': form})
 """
def pagamento_criar_view(request):

    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            # Salvar os dados do formulário
            form.save()
            return redirect('/pagamento')
    else:
        form = PagamentoForm()
    
    return render(request, 'criarPagamento.html', {'form': form})
 