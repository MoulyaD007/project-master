from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handleLogin,name='handleLogin'),
    path('handleLogout',views.handleLogout,name='handleLogout'),
    path('about',views.about,name='about'),
]