from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import FormaPagamento, Pagamento

class FormaPagamentoListView(ListView):
    model = FormaPagamento
    template_name = 'app/forma_pagamento_lista.html'

class FormaPagamentoCreateView(CreateView):
    model = FormaPagamento
    template_name = 'app/forma_pagamento_form.html'
    fields = '__all__'

class FormaPagamentoUpdateView(UpdateView):
    model = FormaPagamento
    template_name = 'app/forma_pagamento_form.html'
    fields = '__all__'

class FormaPagamentoDeleteView(DeleteView):
    model = FormaPagamento
    template_name = 'app/forma_pagamento_confirmar_exclusao.html'
    success_url = reverse_lazy('app:forma_pagamento_lista')


class PagamentoListView(ListView):
    model = Pagamento
    template_name = 'app/pagamento_lista.html'

class PagamentoCreateView(CreateView):
    model = Pagamento
    template_name = 'app/pagamento_form.html'
    fields = '__all__'

class PagamentoUpdateView(UpdateView):
    model = Pagamento
    template_name = 'app/pagamento_form.html'
    fields = '__all__'

class PagamentoDeleteView(DeleteView):
    model = Pagamento
    template_name = 'app/pagamento_confirmar_exclusao.html'
    success_url = reverse_lazy('app:pagamento_lista')
