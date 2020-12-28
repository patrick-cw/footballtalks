"""footballtalks URL Configuration

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
from django.urls import path, include
from main import views

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("register/", views.register,name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("about/", views.about, name="about"),
    path("change_password/", views.change_password, name="change_password"),
    path("upload/", views.upload_file, name="upload"),
    path("news/", views.news, name="news"),
    path('news/<str:slug>/', views.read_article, name="read_article"),
]
