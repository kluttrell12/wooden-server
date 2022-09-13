from rest_framework import serializers, status

from ..models.lumber import Lumber
class LumberSerializer(serializers.ModelSerializer):
    """JSON serializer for Lumber"""
    class Meta:
        model = Lumber
        fields = ('id', 'type')