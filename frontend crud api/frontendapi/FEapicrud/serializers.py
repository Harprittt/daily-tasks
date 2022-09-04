from .models import Novel
from rest_framework import serializers



class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = ['id','title', 'author', 'description', 'publisher']