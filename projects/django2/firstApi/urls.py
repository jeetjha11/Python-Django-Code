from django.contrib import admin
from django.urls import path, include

from .views import get_greet_message, get_user_data, register_user_data

urlpatterns = [
    path('get_message/', get_greet_message),
    path('get_user_data/', get_user_data),
    path('register/', register_user_data),
]
