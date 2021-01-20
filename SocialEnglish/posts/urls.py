from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.PostNew.as_view(), name="new_post"),
    path("group/<str:slug>", views.group_post, name="group_post"),
]
