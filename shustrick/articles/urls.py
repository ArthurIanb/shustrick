from django.urls import path
from .views import index, detail, create, add_comment


app_name = 'articles'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('add_comment/', add_comment, name='add_comment')
]
