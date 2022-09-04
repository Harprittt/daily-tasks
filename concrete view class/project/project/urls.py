from django.contrib import admin
from django.urls import path
from concrete import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/<int:pk>', views.RUDStudentAPI.as_view()),



]
