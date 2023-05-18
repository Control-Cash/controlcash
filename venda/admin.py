from django.contrib import admin

from venda.models import Item, Venda

admin.site.register(Venda)
admin.site.register(Item)
