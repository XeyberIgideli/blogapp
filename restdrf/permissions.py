from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        perms_map = {
            'GET': [],
            'OPTIONS': [],
            'HEAD': [],
            'POST': ['%(app_label)s.add_%(model_name)s'],
            'PUT': ['%(app_label)s.change_%(model_name)s'],
            'PATCH': ['%(app_label)s.change_%(model_name)s'],
            'DELETE': ['%(app_label)s.delete_%(model_name)s'],
         }
    
    # def has_object_permission(self, request, view, obj): 
    #     user = request.user.username
    #     print(user)
    #     if request.method in ('GET', 'HEAD', 'OPTIONS', 'POST'):
    #         return True
    #     return obj.user == request.user