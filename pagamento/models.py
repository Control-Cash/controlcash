from django.db import models

# Create your models here.

# Modelo Pagamento
class Pagamento(models.Model):
    PENDENTE = 'P'
    RECEBIDO = 'R'
    CANCELADO = 'C'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (RECEBIDO, 'Recebido'),
        (CANCELADO, 'Cancelado'),
    ]
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDENTE)
    id_cliente = models.IntegerField()

    def __str__(self):
        return f"Pagamento #{self.id}"