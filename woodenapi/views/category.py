from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from woodenapi.models import Category
from woodenapi.serializers import CategorySerializer

class CategoryView(ViewSet):
    """Viewset for handling category http requests"""

    def list (self, request):
        """method to handle getting all categories"""

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Handle GET request for single category
            Returns:
            Response -- JSON serialized category
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status = status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """method to handle making a new category"""

        category = Category.objects.create(
            type=request.data["type"]
        )

        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """ method to handle updating new category"""

        category = Category.objects.get(pk=pk)
        category.type = request.data["type"]
        category.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk):
        """method to handle deleting a category"""

        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)