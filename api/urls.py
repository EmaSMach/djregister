# --*-- encoding: utf-8 --*--
from django.conf.urls import url
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersAPI)
router.register(r'addresses', views.AddressAPI)
router.register(r'medias', views.MediasAPI)

urlpatterns = router.urls
api_login_pattern = url(r'login/$', views.login, name='api-login')
urlpatterns.append(api_login_pattern)

