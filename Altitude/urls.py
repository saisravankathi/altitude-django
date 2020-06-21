"""Altitude URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import magazine.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', magazine.views.home_page, name="home"),
    path('home', magazine.views.home_page, name="home_redirect"),
    path('story/<str:story_id>', magazine.views.story_detail, name="detail_story"),
    path('publish', magazine.views.create_story_page, name="create_story_page"),
    path('create-story', magazine.views.create_story, name="create_story"),
    path('create-content', magazine.views.create_content_page, name="create_content"),
    path('insert-content', magazine.views.create_content, name="insert content"),
    #path('story', magazine.views.story_page, name="story_page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
