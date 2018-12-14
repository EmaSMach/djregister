"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from rest_framework import routers
import views  # import our custom sign in view to also ask for an email

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^home/', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('profiles.urls')),
    url(r'^$', auth_views.login, name='login'),
    url(r'^register/', views.signup, name='register'),  # use our custom view
    url(r'^logout/', auth_views.logout, name='logout'),

    url(r'^api/', include('api.urls')),
    #url(r'^api/v2/', include('api.urls2')),
]