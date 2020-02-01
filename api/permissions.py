from rest_framework.permissions import BasePermission

class IsStaffOrOwner(BasePermission):
    message = "You must be the owner of staff to access!"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.added_by == request.user):
            return True
        else:
            return False