from rest_framework import serializers, status

from woodenapi.serializers.builder import BuilderSerializer
from woodenapi.serializers.category import CategorySerializer
from woodenapi.serializers.lumber import LumberSerializer
from woodenapi.serializers.tag import TagSerializer



from ..models.project import Project

class ProjectSerializer(serializers.ModelSerializer):
    builder = BuilderSerializer()
    categories = CategorySerializer(many=True)
    tags = TagSerializer(many=True)
    lumber = LumberSerializer(many=True)
    class Meta:
        model = Project
        fields = ('id', 'builder', 'title', 'description', 'date_started', 'date_completed', 'cost', 'image_url', 'approved', 'tags', 'categories', 'lumber')