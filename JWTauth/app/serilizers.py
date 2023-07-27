# Serilizers

from.models import * 
from rest_framework import serializers


class CourseSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class InstructorSer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="course-detail")
    class Meta:
        model = Instructor
        fields = ["name", "courses"]


        
# class CourseSer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = "__all__"

# class InstructorSer(serializers.ModelSerializer):
#     courses = CourseSer(many=True, read_only=True)
#     class Meta:
#         model = Instructor
#         fields = "__all__"