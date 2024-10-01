# input_handler/urls.py

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='input_handler_index'),
]
