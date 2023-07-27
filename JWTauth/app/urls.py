
from django.contrib import admin
from django.urls import path
from .views import * 
urlpatterns = [
    path('instructors',instructorlistview.as_view(),name="instructorlistview"),
    path('courses',courseslistview.as_view(),name="courseslistview"),
    path('courses/<int:pk>',coursedetailview.as_view(),name="course-detail"),
    path('instructors/<int:pk>',instructordetailview.as_view(),name="instructor-detail"),
]
