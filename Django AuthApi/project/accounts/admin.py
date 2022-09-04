from django.contrib import admin
from .models import Register


@admin.register(Register)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
