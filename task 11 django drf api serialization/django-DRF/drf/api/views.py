from django.shortcuts import render, HttpResponse
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer




# Model-object instance display( model-object to serializer to json )


def student_detail(request):
	stu = Student.objects.get(id=2)
	serialize = StudentSerializer(stu)
	json_data = JSONRenderer().render(serialize.data)
	return HttpResponse(json_data, content_type ='application/json')





# Query Set - All Student Data

def student_list(request):
	stu = Student.objects.all()	
	serialize = StudentSerializer(stu, many = True)
	json_data = JSONRenderer().render(serialize.data)
	return HttpResponse(json_data, content_type ='application/json')
