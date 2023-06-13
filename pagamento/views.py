from django.shortcuts import get_object_or_404, render, redirect
from pagamento.models import FormaPagamento, Pagamento
from pagamento.forms import FormaPagamentoForm, PagamentoForm

redirect_response = '/pagamento'

def home_pagamento(request):
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            # Salvar os dados do formulário
            form.save()
            return redirect('/pagamento')
    else:
        form = PagamentoForm()
    
    return render(request, 'criarPagamento.html', {'form': form})
