from django.contrib import admin

from venda.models import Cliente, Item, Venda, Endereco

admin.site.register(Venda)
admin.site.register(Item)
admin.site.register(Cliente)
admin.site.register(Endereco)