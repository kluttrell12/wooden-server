from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from woodenapi.models import Lumber
from woodenapi.serializers import LumberSerializer

class LumberView(ViewSet):
    """Viewset for handling lumber http requests"""

    def list (self, request):
        """method to handle getting all lumber"""

        lumber = Lumber.objects.all()
        serializer = LumberSerializer(lumber, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Handle GET request for single lumber
            Returns:
            Response -- JSON serialized lumber
        """
        try:
            lumber = Lumber.objects.get(pk=pk)
            serializer = LumberSerializer(lumber)
            return Response(serializer.data)
        except Lumber.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status = status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """method to handle making a new lumber"""

        lumber = Lumber.objects.create(
            type=request.data["type"]
        )

        serializer = LumberSerializer(lumber)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """ method to handle updating new lumber"""

        lumber = Lumber.objects.get(pk=pk)
        lumber.type = request.data["type"]
        lumber.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk):
        """method to handle deleting a lumber"""

        lumber = Lumber.objects.get(pk=pk)
        lumber.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)