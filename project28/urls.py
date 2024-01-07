"""
URL configuration for project28 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_topic/',create_topic,name='create_topic'),
    path('create_webpage/',create_webpage,name='create_webpage'),
    path('create_access/',create_access,name='create_access'),
    path('display_webpage/',display_webpage,name='display_webpage'),
    path('select_multiple_webpage/',select_multiple_webpage,name='select_multiple_webpage'),
    path('select_multiple_access/',select_multiple_access,name='select_multiple_access'),
]
