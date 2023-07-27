
from django.contrib import admin
from django.urls import path
from .views import * 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('instructors',instructorlistview.as_view(),name="instructorlistview"),
    path('courses',courseslistview.as_view(),name="courseslistview"),
    path('courses/<int:pk>',coursedetailview.as_view(),name="course-detail"),
    path('instructors/<int:pk>',instructordetailview.as_view(),name="instructor-detail"),
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
