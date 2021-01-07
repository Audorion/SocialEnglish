from django.urls import path
from .models import Post, Group
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<str:slug>", views.group_post, name="group_post")
]
