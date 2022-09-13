from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from woodenapi import serializers
from woodenapi.models import Tag
from woodenapi.serializers import TagSerializer 


class TagView(ViewSet):
    """Viewset for handling tag http requests
    """

    def list(self, request):
        """method to handle getting all tags
        """

        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """method to handle getting single tag by Id"""
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status = status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """method to handle making a new tag"""

        tag = Tag.objects.create(
            label=request.data["label"]
        )

        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def update(self, request, pk):
        """method to handle editing a tag"""

        tag = Tag.objects.get(pk=pk)
        tag.label=request.data["label"]
        tag.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """method to handle deleting a tag"""

        tag = Tag.objects.get(pk = pk)
        tag.delete() 
        return Response(None, status=status.HTTP_204_NO_CONTENT)