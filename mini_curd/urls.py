"""mini_curd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from mini_curd import views as mini_views
from app_curd import views as curd_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mini_views.login),
    path('login/', mini_views.login),
    path('logout/', mini_views.logout),
    path('index/', curd_views.index),
    
    # path('test/', mini_views.test),
]
