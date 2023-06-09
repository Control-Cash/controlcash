from django.shortcuts import get_object_or_404, render, redirect
from pagamento.models import FormaPagamento, Pagamento
from pagamento.forms import FormaPagamentoForm, PagamentoForm

redirect_response = '/pagamento'

def home_pagamento(request):
    pagamentos = Pagamento.objects.all()
    return render(request, "home.html", {"pagamentos": pagamentos} )

def view_criar_pagamento(request):
    form = PagamentoForm()
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_response)

    return render(request,'formEditarPagamento.html', {"form": form})
