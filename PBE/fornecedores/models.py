# fornecedores/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Fornecedor(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='fornecedor'
    )
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    #nif = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    
    def __str__(self):
        return self.nome_empresa
    
class Encomenda(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('processando', 'Processando'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    
    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='encomendas')
    fornecedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='encomendas_fornecedor')
    data_criacao = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    
    class Meta:
        ordering = ['-data_criacao']
    
    def __str__(self):
        return f"Encomenda #{self.numero}"
    
    @property
    def status_cor(self):
        cores = {
            'pendente': 'warning',
            'processando': 'info',
            'enviado': 'primary',
            'entregue': 'success',
            'cancelado': 'danger',
        }
        return cores.get(self.status, 'secondary')