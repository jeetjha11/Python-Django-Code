from django.contrib import admin
from django.urls import path

from .views import product_view, filter_view

urlpatterns = [
    path('product_operation/', product_view),
    path('product_filter/', filter_view),

]
