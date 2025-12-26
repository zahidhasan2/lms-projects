from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import CourseCategory, Course, Enrollment
from .serializers import CourseCategorySerializer, CourseSerializer, EnrollmentSerializer
from .permissions import IsInstructorOrAdminForCourse
from .reports import get_dashboard_stats

User = get_user_model()

class CourseCategoryViewSet(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ("GET",):
            return [AllowAny()]
        from accounts.permissions import IsAdmin
        return [IsAdmin()]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().select_related("category", "instructor")
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsInstructorOrAdminForCourse]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if not user.is_authenticated:
            return qs.filter(is_published=True)
        if user.role == "instructor":
            return qs.filter(instructor=user)
        if user.role == "student":
            return qs.filter(is_published=True)
        return qs

    def perform_create(self, serializer):
        serializer.save()

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all().select_related("course", "student")
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "student":
            return self.queryset.filter(student=user)
        if user.role == "instructor":
            return self.queryset.filter(course__instructor=user)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def stats(self, request):
        from accounts.permissions import IsAdmin
        if not IsAdmin().has_permission(request, self):
            return Response({"detail": "Forbidden."}, status=status.HTTP_403_FORBIDDEN)
        stats = get_dashboard_stats()
        return Response(stats)
