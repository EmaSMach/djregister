# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from .serializers import AddressSerializer, UsersSerializer, MediasSerializer
from profiles.models import Address, Users, Medias


#@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    A login view for the api.
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class AddressAPI(viewsets.ModelViewSet):
    """
    An api view for the address data.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UsersAPI(viewsets.ModelViewSet):
    """
    An api view for the address data.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class MediasAPI(viewsets.ModelViewSet):
    """
    An api view for the address data.
    """
    queryset = Medias.objects.all()
    serializer_class = MediasSerializer
