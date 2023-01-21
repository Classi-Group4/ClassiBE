from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from class_reservation import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'classes', views.ClassViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_frameworks')),
]

