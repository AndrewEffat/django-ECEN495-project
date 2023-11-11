from django.contrib import admin
from django.urls import path, include
from item.views import ItemViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", ItemViewset, basename="item")

urlpatterns = [
    path("item/", include(router.urls))
]