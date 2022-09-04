from django.urls import path
from . import views



urlpatterns = [

path('studata/', views.student_list),
path('studata/<int:id>', views.student_detail),





]