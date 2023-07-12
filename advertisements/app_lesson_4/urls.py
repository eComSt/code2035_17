from django.contrib import admin
from django.urls import path
from .views import lesson_4

urlpatterns = [
    path("lesson_4/",lesson_4),
]
