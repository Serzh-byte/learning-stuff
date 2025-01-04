"""
URL configuration for something project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', views.simple, name='studying'),
    path('forms/', views.forms, name='forms'),
    path('home/', views.home, name='home'),
    path('name/', views.name, name='name'),
    path('bt1/', views.bt1, name='bt1'),
    path('bt2/', views.bt2, name='bt2'),
    path('', views.all, name='all'),
    path('cards/', views.cards, name='cards'),
    path('navbar/', views.navbar, name='navbar'),
]
