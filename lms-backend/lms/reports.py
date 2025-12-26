from django.contrib.auth import get_user_model
from django.db.models import Count
from .models import Course, Enrollment

User = get_user_model()

def get_dashboard_stats():
    total_users = User.objects.count()
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()
    role_counts = User.objects.values("role").annotate(count=Count("id"))
    return {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_enrollments": total_enrollments,
        "role_counts": {item["role"]: item["count"] for item in role_counts},
    }
