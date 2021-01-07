
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("posts.urls")),
    path("auth/", include("registration.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('group/', include("posts.urls"))
]
