# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from profiles.models import Address, Users, Medias


class AddressSerializer(serializers.ModelSerializer):
    """
    Serialize the address data.
    """
    class Meta:
        model = Address
        fields = ('address', 'city', 'state', 'country', 'zip_code')


class MediasSerializer(serializers.ModelSerializer):
    """
    Serialize the medias data.
    """
    class Meta:
        model = Medias
        fields = ('url',)


class UsersSerializer(serializers.ModelSerializer):
    """
    Serialize the user data.
    """
    address = AddressSerializer(many=True)
    socials = MediasSerializer(many=True)

    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'age',
            'gender',
            'email',
            'active',
            'address',
            'socials',
            'phone_number',
            'timezone',
        ]
