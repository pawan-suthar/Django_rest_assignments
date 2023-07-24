from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course
from .courseserializer import CourseSerializer

# Create your views here.
@api_view(["GET","POST"])
def courselistview(request):
    if request.method == "GET":
        allcourses = Course.objects.all() #sare course laao
        ser = CourseSerializer(allcourses,many=True) # serlizse kro
        return Response(ser.data) # return object
    elif request.method == "POST":
        ser = CourseSerializer(data=request.data)
        if ser.is_valid(): #if valid
            ser.save() #save data in python obj
            return Response(ser.data, status=status.HTTP_201_CREATED) #return serliazied data
        return Response(ser.errors)


    
@api_view(["GET","PUT","DELETE"])
def coursedetailview(request,pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        ser = CourseSerializer(course)
        return Response(ser.data)
    

    elif request.method == "PUT":
         ser = CourseSerializer(course,data=request.data)
         if ser.is_valid():
             ser.save()
             return Response(ser.data)
         return Response(ser.errors)
    
    
    elif request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


