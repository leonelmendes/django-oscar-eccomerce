from django.db import models
from users.models import FornecedorProfile
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

UNIDADES = [
    ('m2', 'Metro quadrado (m²)'),
    ('m3', 'Metro cúbico (m³)'),
    ('saco', 'Saco'),
    ('kg', 'Quilograma (kg)'),
    ('unid', 'Unidade'),
]

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_venda = models.CharField(max_length=10, choices=UNIDADES)
    quantidade = models.PositiveIntegerField(default=0)
    fornecedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    def __str__(self):
        return self.nome
