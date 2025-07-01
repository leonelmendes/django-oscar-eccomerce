from produtos.models import Produto

class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get('carrinho')
        if not carrinho:
            carrinho = self.session['carrinho'] = {}
        self.carrinho = carrinho

    def add(self, produto_id, quantidade=1):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            self.carrinho[produto_id]['quantidade'] += quantidade
        else:
            self.carrinho[produto_id] = {'quantidade': quantidade}
        self.save()

    def remove(self, produto_id):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.save()

    def clear(self):
        self.session['carrinho'] = {}
        self.session.modified = True

    def save(self):
        self.session.modified = True

    def __iter__(self):
        produto_ids = self.carrinho.keys()
        produtos = Produto.objects.filter(id__in=produto_ids)
        carrinho = self.carrinho.copy()

        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto
            carrinho[str(produto.id)]['subtotal'] = (
                produto.preco * carrinho[str(produto.id)]['quantidade']
            )
            yield carrinho[str(produto.id)]

    def get_total(self):
        return sum(
            item['produto'].preco * item['quantidade']
            for item in self.__iter__()
        )
