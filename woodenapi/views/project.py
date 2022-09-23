from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from woodenapi.models.builder import Builder

from woodenapi.models.project import Project
from woodenapi.serializers.project import ProjectSerializer

class ProjectView(ViewSet):
    def list(self, request):
        """handle get all project.approved = true"""
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """handle get requests for single project"""
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def create(self, request):
        """handles creating a new project"""
        user = request.auth.user
        builder = Builder.objects.get(user__id = user.id)
        if user.is_staff == True :
            project = Project.objects.create(
                builder = builder,
                title = request.data['title'],
                description = request.data['description'],
                date_started = request.data['date_started'],
                date_completed = request.data['date_completed'],
                cost = request.data['cost'],
                image_url = request.data['image_url']
            )
        else :
            project = Project.objects.create(
                builder = builder,
                title = request.data['title'],
                description = request.data['description'],
                date_started = request.data['date_started'],
                date_completed = request.data['date_completed'],
                cost = request.data['cost'],
                image_url = request.data['image_url']
            )
        project.tags.add(*request.data['tags'])
        project.categories.add(*request.data['categories'])
        project.lumber.add(*request.data['lumber'])

        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """function to update project"""

        project = Project.objects.get(pk=pk)
        project.title = request.data['title']
        project.description = request.data['description']
        project.date_started = request.data['date_started']
        project.date_completed = request.data['date_completed']
        project.cost = request.data['cost']
        project.image_url = request.data['image_url']
        project.save()
        project.tags.clear()
        project.categories.clear()
        project.lumber.clear()
        project.tags.add(*request.data['tags'])
        project.categories.add(*request.data['categories'])
        project.lumber.add(*request.data['lumber'])
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        """function to delete projects"""
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
