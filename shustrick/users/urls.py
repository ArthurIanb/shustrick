from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, UserLogin, logout_user, detail


app_name = "users"
urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('detail/<int:pk>/', detail, name='detail'),
]
