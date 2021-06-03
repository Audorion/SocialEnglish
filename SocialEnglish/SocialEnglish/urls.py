
from django.contrib import admin
from django.urls import include, path
from django.contrib.flatpages import views

urlpatterns = [
    path("", include("posts.urls")),
    path("about/", include('django.contrib.flatpages.urls')),
    path("auth/", include("registration.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += [
        path('about-us/', views.flatpage, {'url': 'about-us/'}, name='about-us'),
        path('terms/', views.flatpage, {'url': '/terms/'}, name='terms'),
        path('about-author/', views.flatpage, {'url': '/about-author/'}, name='about-author'),
        path('about-spec/', views.flatpage, {'url': 'about-spec/'}, name='about-spec'),
]