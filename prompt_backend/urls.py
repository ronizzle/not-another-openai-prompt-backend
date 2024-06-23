from django.contrib import admin
from django.urls import path
from .views import generate_answer

urlpatterns = [
    path('ask', generate_answer, name='ask'),
]