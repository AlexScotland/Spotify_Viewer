"""spotify_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from web import views as web_views
from spotify_web_api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'current_song', views.SpotifyData, basename="current song")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web_views.index),
    path('api/', include((router.urls))),
    path('current_song', web_views.view_song, name='current_song'),
]
