from django.urls import path
from .views import obtener_posts

urlpatterns = [
    path('posts/', obtener_posts),
]