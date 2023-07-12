from django.shortcuts import get_object_or_404, render, redirect

from pagamento.models import Pagamento
from pagamento.forms import PagamentoForm

redirect_response = '/pagamento'

SUCCESS_REDIRECT_URL = 'pagamento:home_pagamento'

def home_pagamento_view(request):
    pagamento = Pagamento.objects.all()
    return render(request, 'home_pagamento.html', {"pagamento": pagamento})

def criar_pagamento_view(request):

    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pagamento')
    else:
        form = PagamentoForm()
    
    return render(request, 'criar_pagamento.html', {'form': form})

def editar_pagamento_view(request, pk):
    pagamento_obj = get_object_or_404(Pagamento, id=pk)
    form = PagamentoForm(instance=pagamento_obj)

    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento_obj)
        if form.is_valid():
            form.save()
            return redirect(SUCCESS_REDIRECT_URL)
    return render(request, 'editar_pagamento.html', {'form': form})

def remover_pagamento_view(request, pk):
    pagamento = get_object_or_404(Pagamento, id=pk)
    if request.method == 'POST':
        pagamento.delete()
        return redirect(SUCCESS_REDIRECT_URL)
    return render(request, 'remover_pagamento.html', {'pagamento': pagamento})

 
