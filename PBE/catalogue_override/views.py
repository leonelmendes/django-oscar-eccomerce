from django.shortcuts import render
from django.views.generic import ListView
from produtos.models import Produto, Categoria
from django.views.generic import TemplateView
# Create your views here.

#class CustomCatalogueView(ListView):
    #model = Produto
    #template_name = 'oscar/catalogue/browse.html'
    #context_object_name = 'products'
    # paginate_by = 12  # Número de produtos por página

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     category_slug = self.request.GET.get('category')  # Obtém o slug da categoria da query string

    #     if category_slug:
    #         queryset = queryset.filter(categoria__slug=category_slug)  # Filtra produtos pela categoria
        
    #     return queryset.order_by('nome')  # Ordena os produtos pelo nome

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Categoria.objects.all()  # Adiciona todas as categorias ao contexto
    #     context['current_category'] = self.request.GET.get('category')  # Adiciona a categoria atual ao contexto
    #    return context
    
class CustomCatalogueView(TemplateView):
    template_name = 'oscar/catalogue/browse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.request.GET.get('category')

        if categoria_id:
            produtos = Produto.objects.filter(categoria_id=categoria_id)
        else:
            produtos = Produto.objects.all()

        context['products'] = produtos
        context['categories'] = Categoria.objects.all()
        return context