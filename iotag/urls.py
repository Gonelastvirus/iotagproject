"""iotag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from iotapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('settings/',views.settings,name='settings'),
    path('soiltempdata/',views.soiltempdata,name='soiltempdata'),
     path('recentactivity/',views.recentactivity,name='recentactivity'),
    path("permission_denied/",views.permission_denied,name="permission_denied"),
]
urlpatterns += staticfiles_urlpatterns()

