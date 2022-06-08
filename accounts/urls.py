# 127.0.0.1/account/login
from django.urls import path

from accounts import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.user_profile, name='profile'),
]
