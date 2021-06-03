from django.urls import path
from . import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path("", views.PostList.as_view(), name="index"),
    path("new/", views.PostNew.as_view(), name="new_post"),
    path("post/<slug:slug>/", views.ShowPost.as_view(), name="post_detail"),
    #path('<str:username>/', views.profile, name='profile'),
   # path('<str:username>/<int:post_id>/', views.post_view, name='post'),
    #path(
    #   '<str:username>/<int:post_id>/edit/',
    #   views.post_edit,
    #   name='post_edit'
    #    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
