from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CourseCategory, Course, Enrollment

User = get_user_model()

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ["id", "name", "description"]

class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=CourseCategory.objects.all(),
        source="category",
        write_only=True
    )
    instructor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "category",
            "category_id",
            "instructor",
            "is_published",
            "created_at",
        ]

    def create(self, validated_data):
        instructor = self.context["request"].user
        return Course.objects.create(instructor=instructor, **validated_data)

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source="course", write_only=True
    )

    class Meta:
        model = Enrollment
        fields = ["id", "course", "course_id", "enrolled_at"]
