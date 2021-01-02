"""personalWebpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from baseApp import views as base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view.experience, name='experience'),
    path('links/', base_view.links, name='links'),
    path('gallery', base_view.gallery, name='gallery'),
    path('photoOfTheDay/', base_view.photo_of_the_day, name='potd'),
    path('about/', base_view.about, name='about'),
    path('contact/', base_view.contact, name='contact'),
]
