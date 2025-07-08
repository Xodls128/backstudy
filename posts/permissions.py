from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):#작성자 외에는 읽기만 가능
    def has_object_permission(self, request, view, obj):
       
        if request.method in permissions.SAFE_METHODS: #SAFE_METHODS(보안위협없는) :GET, HAED, OPTIONS
            return True
        return obj.author == request.user
    
    