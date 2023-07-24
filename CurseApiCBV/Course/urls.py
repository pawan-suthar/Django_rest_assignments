
from django.contrib import admin
from django.urls import path
from app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/course', v.CourseListView.as_view(), name="listview"),
]
