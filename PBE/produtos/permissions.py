from rest_framework import permissions

class IsFornecedorOwnerOrReadOnly(permissions.BasePermission):
    """
    - SAFE methods: todos podem ler.
    - Métodos de escrita: só fornecedor dono do produto.
    """
    def has_permission(self, request, view):
        # criar só se for fornecedor autenticado
        if view.action == 'create':
            return request.user.is_authenticated and request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and obj.fornecedor == request.user