from django.urls import path
from .views import index, detail, create


app_name = 'articles'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('create/', create, name='create'),
]
