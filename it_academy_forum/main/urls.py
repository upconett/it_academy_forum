from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirector),
    path('login/', views.login),
    path('register/', views.register),
    path('home/', views.home)
]
