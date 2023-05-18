from django.db import models


class Venda(models.Model):
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    # cliente = models.ForeignKey()
    # vendedor = models.ForeignKey()
