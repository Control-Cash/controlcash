from django.db import models

class Pagamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('recebido', 'Recebido'),
        ('cacelado', 'Cancelado'),
    ]
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pendente')
    id_cliente = models.IntegerField()

    def __str__(self):
        return f"Pagamento #{self.id}"
