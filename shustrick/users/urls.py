from django.urls import path
from .views import login_user, logout_user, register

app_name = "users"
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]


