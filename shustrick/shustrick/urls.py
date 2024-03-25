from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls', namespace='article')),
    path('users/', include('users.urls', namespace='users')),
]
