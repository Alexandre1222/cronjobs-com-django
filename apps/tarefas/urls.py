from django.contrib import admin
from django.urls import path
from apps.tarefas.views import index

urlpatterns = [
    path('', index),
]
