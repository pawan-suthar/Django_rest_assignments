# Serilizers

from.models import * 
from rest_framework import serializers

class CourseSer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class InstructorSer(serializers.ModelSerializer):
    courses = CourseSer(many=True, read_only=True)
    class Meta:
        model = Instructor
        fields = "__all__"