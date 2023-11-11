from django.contrib import admin
from django.urls import path, include
from category.views import CategoryViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", CategoryViewset, basename="category")

urlpatterns = [
    path("category/", include(router.urls))
]