from django.core.validators import MinValueValidator
from django.db import models


class Despesa(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                MinValueValidator(0.01)])
    periodica = models.BooleanField(verbose_name="periódica", default=False)

    def __str__(self) -> str:
        return f"{self.nome}"
