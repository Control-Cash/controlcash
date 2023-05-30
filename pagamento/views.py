from django.shortcuts import render

# Create your views here.

def home_pagamento(request):
    return render(request, 'lista_pagamento.html')
