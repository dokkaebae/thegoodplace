from django.contrib import admin
from django.urls import path

from .views import go_to_home_page

urlpatterns = [
    path('', go_to_home_page),
]
