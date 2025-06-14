from oscar.apps.catalogue.abstract_models import AbstractProduct
from django.conf import settings
from django.db import models

class Product(AbstractProduct):
    fornecedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Fornecedor"
    )

from oscar.apps.catalogue.models import * # importa todos os outros modelos padrão