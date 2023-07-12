from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods

from pagamento.models import Pagamento
from pagamento.forms import PagamentoForm

redirect_response = '/pagamento'

SUCCESS_REDIRECT_URL = 'pagamento:home_pagamento'

@require_http_methods(["GET"])
def home_pagamento_view(request):
    pagamento = Pagamento.objects.all()
    return render(request, 'home_pagamento.html', {"pagamento": pagamento})

@require_http_methods(["GET", "POST"])
def criar_pagamento_view(request):
    form = PagamentoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(SUCCESS_REDIRECT_URL)
    return render(request, 'criar_pagamento.html', {'form': form})

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

@require_http_methods(["GET", "POST"])
def remover_pagamento_view(request, pk):
    pagamento = get_object_or_404(Pagamento, id=pk)
    if request.method == 'POST':
        pagamento.delete()
        return redirect(SUCCESS_REDIRECT_URL)
    return render(request, 'remover_pagamento.html', {'pagamento': pagamento})

 
