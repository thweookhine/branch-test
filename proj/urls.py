
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.db import router
from app import views

router = routers.DefaultRouter()
router.register(r'songs',views.SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
]
