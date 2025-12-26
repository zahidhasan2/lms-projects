from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsInstructorOrAdminForCourse(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return user.is_authenticated and (user.role == "admin" or obj.instructor_id == user.id)
