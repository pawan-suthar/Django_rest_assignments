from django.shortcuts import render
from requests import request
from .models import Course, CourseSerializer
from rest_framework import mixins, generics #used to get handler methods
class CourseListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class CourseDetailView(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)







# using apiview base class

# class CourseListView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         ser = CourseSerializer(data = request.data)
#         if ser.is_valid(): #if valid
#             ser.save() #save data in python obj
#             return Response(ser.data, status=status.HTTP_201_CREATED) #return serliazied data
#         return Response(ser.errors)
# class CourseDetailView(APIView):
#     def get_course(self,pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404
#     def get(self,request,pk):
#         courses = self.get_course(pk)
#         ser  = CourseSerializer(courses)
#         return Response(ser.data)
#     def put(self,request,pk):
#         course = self.get_course(pk)
#         ser = CourseSerializer(course,data = request.data)
#         if ser.is_valid(): #if valid
#             ser.save() #save data in python obj
#             return Response(ser.data) #return serliazied data
#         return Response(ser.errors)
#     def delete(self,request,pk):
#         self.get_course(pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)