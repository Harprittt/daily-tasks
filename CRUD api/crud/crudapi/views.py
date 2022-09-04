from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.http import HttpResponse
from . models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_data(request):
	if request.method == 'GET':
		json_data = request.body             #it will store jsondata given by client in json_data variable
		stream = io.BytesIO(json_data)                     #it will store data into the memory
		pythondata = JSONParser().parse(stream)                 #it will convert json into python
		id = pythondata.get('id', None)			                    #it will get data from db even its model object or queryset

		if id is not None: 						        #if client want particular data 
			stu = Student.objects.get(id=id)	             #then it will get particular data from db
			serialize = StudentSerializer(stu)	                 #again converted into 
			json_data = JSONRenderer().render(serialize.data)		    #it will return json data 
			return HttpResponse(json_data, content_type = 'application/json')

		stu = Student.objects.all()
		serialize = StudentSerializer(stu, many = True)
		json_data = JSONRenderer().render(serialize.data)
		return HttpResponse(json_data, content_type = 'application/json')

	return HttpResponse("try again")


