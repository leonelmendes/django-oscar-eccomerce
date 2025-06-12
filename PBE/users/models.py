from django.db import models
from django.contrib.auth.models import User

class FornecedorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Fornecedor: {self.user.username}, Empresa: {self.empresa}"

class ClienteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Cliente: {self.user.username}"

