# fornecedores/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Fornecedor(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='fornecedor'
    )
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    
    def __str__(self):
        return self.nome_empresa