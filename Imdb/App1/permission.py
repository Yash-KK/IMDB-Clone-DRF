from rest_framework import permissions

class isAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_related = bool(request.user and request.user.is_staff)
        return request.method == 'GET' or admin_related

class isOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  
        
        return obj.review_user == request.user or request.user.is_staff
    
    