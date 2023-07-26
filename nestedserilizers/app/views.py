from django.shortcuts import render
from rest_framework import generics
from .serilizers import * 
from .models import * 


class instructorlistview(generics.ListCreateAPIView):
    serializer_class = InstructorSer
    queryset = Instructor.objects.all()

class courseslistview(generics.ListCreateAPIView):
    serializer_class = CourseSer
    queryset = Course.objects.all()