from django.shortcuts import render

from despesa.models import Despesa


def listar_despesas_view(request):
    despesas = Despesa.objects.all()
    return render(request, 'despesa/listar.html', {"despesas": despesas})
