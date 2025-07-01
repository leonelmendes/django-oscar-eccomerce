from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.db import transaction
from .cart import Carrinho
from produtos.models import Produto
from fornecedores.models import Encomenda

@login_required
def adicionar_ao_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    carrinho.add(produto_id, quantidade=1)
    return redirect('carrinho:ver-carrinho')

@login_required
def remover_do_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    carrinho.remove(produto_id)
    return redirect('carrinho:ver-carrinho')

@login_required
def ver_carrinho(request):
    carrinho = Carrinho(request)
    return render(request, 'carrinho/basket.html', {'carrinho': carrinho})

@login_required
@transaction.atomic
def finalizar_compra(request):
    carrinho = Carrinho(request)
    cliente = request.user

    for item in carrinho:
        produto = item['produto']
        quantidade = item['quantidade']

        if produto.quantidade < quantidade:
            messages.error(request, f"Sem stock para {produto.nome}")
            return redirect('carrinho:ver-carrinho')

        # Criar encomenda para cada produto
        Encomenda.objects.create(
            numero=get_random_string(10).upper(),
            cliente=cliente,
            fornecedor=produto.fornecedor,
            total=produto.preco * quantidade,
            status='pendente'
        )

        produto.quantidade -= quantidade
        produto.save()

    carrinho.clear()
    messages.success(request, "Compra finalizada com sucesso!")
    return redirect('catalogue:browse')
