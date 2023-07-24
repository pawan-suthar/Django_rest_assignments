
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/course', views.courselistview, name="listview"),
    path('api/course/<int:pk>', views.coursedetailview, name="detailview"),
]
