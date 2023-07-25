
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
# from app import views as v
from app.views import CourseViewSet

router = DefaultRouter()
router.register('course',CourseViewSet,basename="viewset")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
    # path('api/', include('app.urls')),
   
]
