from rest_framework import permissions

def is_editor(user):
    return bool(user and user.is_authenticated and user.groups.filter(name="Editor").exists())

class IsPortfolioRolePermission(permissions.BasePermission):
    """
    Role-Based Access Control (RBAC) 4 Peran Pengguna:
    1. Guest (Unauthenticated): Hanya dapat membaca data (GET, HEAD, OPTIONS).
    2. Regular Authenticated User: Membaca data dan toggle star; dilarang create/edit/delete.
    3. Editor (Anggota Grup 'Editor'): Membaca data, toggle star, dan memperbarui data (PUT, PATCH); dilarang create/delete.
    4. Superuser: Akses penuh CRUD dan toggle star.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        if is_editor(request.user):
            return request.method in ['PUT', 'PATCH']

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        if is_editor(request.user):
            return request.method in ['PUT', 'PATCH']

        return False
