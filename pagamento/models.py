from django.db import models

# Create your models here.


# Modelo Forma de Pagamento

class FormaPagamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    taxas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    
# Modelo Pagamento
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