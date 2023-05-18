from django.shortcuts import render

from venda.models import Venda


def listar_vendas_view(request):
    vendas = Venda.objects.all()
    return render(request, 'venda/listar_vendas.html', {'vendas': vendas})
