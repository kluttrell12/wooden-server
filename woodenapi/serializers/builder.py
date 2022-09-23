from django.db import models
from rest_framework import serializers, status
from django.contrib.auth.models import User
from woodenapi.models.builder import Builder

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'is_staff',
            'is_active'
            )
class BuilderSerializer(serializers.ModelSerializer):
    user=UserSerializer()

    class Meta:
        model = Builder
        fields = ('id', 'user')

class UserDetailedSerializer(serializers.ModelSerializer):
    """
    serializer to get more detailed information for user profiles
    """
    class Meta:
        model = User
        fields = (
        'first_name',
        'last_name',
        'username',
        'email',
        'is_staff'
        )

class BuilderDetailedSerializer(serializers.ModelSerializer):
    """
    serializer to get more detailed information for user profile
    """
    user=UserSerializer()
    class Meta:
        model = Builder
        fields = (
        'id',
        'user',
        'profile_image_url',
        'bio'
        )