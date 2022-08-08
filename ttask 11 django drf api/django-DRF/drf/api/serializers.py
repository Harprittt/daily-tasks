from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=30)
	roll = serializers.IntegerField()
	city = serializers.CharField(max_length=30)