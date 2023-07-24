from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, CourseSerializer

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)