from django.urls import path
from . import views



urlpatterns = [

path('stuinfo/', views.student_detail),
path('stulist/', views.student_list)




]