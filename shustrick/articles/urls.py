from django.urls import path
from .views import index, detail, create, add_comment, delete, set_status


app_name = 'articles'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('add_comment/', add_comment, name='add_comment'),
    path('delete/<int:article_pk>/', delete, name="delete"),
    path('set_status/<int:article_pk>/<str:status>/', set_status, name="set_status"),
]
