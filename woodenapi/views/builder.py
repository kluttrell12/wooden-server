from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from woodenapi.models.builder import Builder
from woodenapi.serializers.builder import BuilderDetailedSerializer, BuilderSerializer
from rest_framework.decorators import action

class BuilderView(ViewSet):
    """
    ViewSet that handles user requests
    """

    def retrieve(self, request, pk):
        """method to handle returning details of a single user"""

        builder = Builder.objects.get(pk = pk)
        serializer = BuilderDetailedSerializer(builder)
        return Response(serializer.data)

    def list(self, request):
        """method to handle returning of all users"""

        builders = Builder.objects.all()
        serializer = BuilderSerializer(builders, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """method to handle updating user's information"""
        builder = Builder.objects.get(pk = pk)
        user = User.objects.get(pk=builder.user.id)

        user.first_name = request.data["user"]["first_name"]
        user.last_name = request.data["user"]["last_name"]
        user.username = request.data["user"]["username"]
        user.email = request.data["user"]["email"]
        user.is_staff = request.data["user"]["is_staff"]
        user.is_active = request.data["user"]["is_active"]
        builder.bio = request.data["bio"]

        user.save()
        builder.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods = ['get'], detail=False)
    def active(self, request):

        """method to handle returning ONLY ACTIVE USERS"""
        user = Builder.objects.get(user = request.auth.user)

        """method to handle returning a list of all ACTIVE users"""

        builders = Builder.objects.all().order_by("user__username")
        builders = builders.filter(user__is_active = True)
        for builder in builders:
            builder.following = user
        serializer = BuilderSerializer(builders, many=True)
        return Response(serializer.data)

    @action(methods = ['get'], detail=False)
    @action(methods = ['get'], detail=False)
    def inactive(self, request):
        """method to handle returning a list of all INACTIVE users"""

        builders = Builder.objects.all().order_by("user__username")
        builders = builders.filter(user__is_active = False)
        serializer = BuilderSerializer(builders, many=True)
        return Response(serializer.data)

    @action(methods = ['put'], detail=True)
    def active_status(self, request, pk):
        """method to handle toggling a user's "is_active" status between true and false."""

        builder = Builder.objects.get(pk=pk)
        user = User.objects.get(pk=builder.user.id)
        user.is_active = not user.is_active
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
