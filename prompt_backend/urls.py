from django.contrib import admin
from django.urls import path
from .views import generate_answer, generate_answer_realtime

urlpatterns = [
    path('ask', generate_answer, name='ask'),
    path('ask-realtime', generate_answer_realtime, name='ask-realtime'),
]