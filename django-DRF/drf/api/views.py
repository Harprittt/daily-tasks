from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def student_list(request):

	#get all student list
	#serialize them
	#return json

	if request.method == 'GET':
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many = True)
		return Response(serializer.data)

	if request.method == 'POST':
		serializer = StudentSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):

	try:
		stu = Student.objects.get(pk=id)
	except Student.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = StudentSerializer(stu)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = StudentSerializer(stu, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	elif request.method == 'DELETE':
		stu.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
