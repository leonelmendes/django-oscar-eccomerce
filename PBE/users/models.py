from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class FornecedorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Fornecedor: {self.user.username}, Empresa: {self.empresa}"

class ClienteProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Cliente: {self.user.username}"

class User(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    tipo = models.CharField(max_length=20, choices=[
        ('cliente', 'Cliente'),
        ('fornecedor', 'Fornecedor')
    ], default='cliente')